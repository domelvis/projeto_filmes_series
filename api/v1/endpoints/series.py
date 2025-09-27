from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q

from series.models import Serie
from api.v1.serializers.series import (
    SerieSerializer,
    SerieListSerializer,
    SerieCreateUpdateSerializer
)
from api.v1.permissions import IsOwnerOrReadOnly


class SerieViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar séries.
    
    Permite:
    - Listar todas as séries (público)
    - Criar nova série (autenticado)
    - Visualizar detalhes de uma série (público)
    - Atualizar série (apenas o criador)
    - Deletar série (apenas o criador)
    """
    
    queryset = Serie.objects.all().order_by('-data_criacao')
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['genero', 'ano', 'criado_por']
    search_fields = ['titulo', 'descricao']
    ordering_fields = ['titulo', 'ano', 'data_criacao', 'data_atualizacao']
    ordering = ['-data_criacao']
    
    def get_serializer_class(self):
        """Retorna o serializer apropriado para cada ação"""
        if self.action == 'list':
            return SerieListSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return SerieCreateUpdateSerializer
        return SerieSerializer
    
    def get_queryset(self):
        """Filtra o queryset baseado nos parâmetros"""
        queryset = super().get_queryset()
        
        # Filtro por ano
        ano_min = self.request.query_params.get('ano_min')
        ano_max = self.request.query_params.get('ano_max')
        
        if ano_min:
            queryset = queryset.filter(ano__gte=ano_min)
        if ano_max:
            queryset = queryset.filter(ano__lte=ano_max)
        
        # Filtro por usuário
        usuario = self.request.query_params.get('usuario')
        if usuario:
            queryset = queryset.filter(criado_por__username=usuario)
        
        return queryset
    
    def perform_create(self, serializer):
        """Define o usuário atual como criador da série"""
        serializer.save(criado_por=self.request.user)
    
    @action(detail=False, methods=['get'])
    def minhas_series(self, request):
        """Retorna as séries criadas pelo usuário atual"""
        if not request.user.is_authenticated:
            return Response(
                {'detail': 'Autenticação necessária.'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        series = self.get_queryset().filter(criado_por=request.user)
        serializer = self.get_serializer(series, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def favoritar(self, request, pk=None):
        """Adiciona/remove série dos favoritos (funcionalidade futura)"""
        serie = self.get_object()
        # Aqui você pode implementar a lógica de favoritos
        return Response({
            'detail': 'Funcionalidade de favoritos será implementada em breve.'
        })
    
    @action(detail=False, methods=['get'])
    def estatisticas(self, request):
        """Retorna estatísticas das séries"""
        total_series = Serie.objects.count()
        series_por_genero = {}
        
        for genero, _ in Serie.GENERO_CHOICES:
            count = Serie.objects.filter(genero=genero).count()
            if count > 0:
                series_por_genero[genero] = count
        
        return Response({
            'total_series': total_series,
            'series_por_genero': series_por_genero,
            'series_recentes': Serie.objects.count()  # Últimas 7 dias
        })
    
    @action(detail=True, methods=['get'])
    def relacionadas(self, request, pk=None):
        """Retorna séries relacionadas (mesmo gênero)"""
        serie = self.get_object()
        relacionadas = Serie.objects.filter(
            genero=serie.genero
        ).exclude(id=serie.id)[:4]
        
        serializer = SerieListSerializer(relacionadas, many=True, context={'request': request})
        return Response(serializer.data)

