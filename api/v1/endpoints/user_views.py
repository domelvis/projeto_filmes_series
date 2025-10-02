from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from api.v1.serializers.user_serializers import UserSerializer, UserActivitySerializer
from users.models import UserActivity

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    def get_object(self):
        return self.request.user

    @action(detail=False, methods=['post'])
    def change_password(self, request):
        user = request.user
        current_password = request.data.get('current_password')
        new_password = request.data.get('new_password1')
        confirm_password = request.data.get('new_password2')

        if not user.check_password(current_password):
            return Response(
                {'error': 'Senha atual incorreta'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if new_password != confirm_password:
            return Response(
                {'error': 'As senhas não conferem'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user.set_password(new_password)
        user.save()
        return Response({'message': 'Senha alterada com sucesso'})

    @action(detail=False, methods=['post'])
    def upload_image(self, request):
        user = request.user
        if 'profile_image' not in request.FILES:
            return Response(
                {'error': 'Nenhuma imagem enviada'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user.profile_image = request.FILES['profile_image']
        user.save()
        return Response(UserSerializer(user).data)

    @action(detail=False, methods=['delete'])
    def delete_image(self, request):
        user = request.user
        if user.profile_image:
            user.profile_image.delete()
        user.profile_image = None
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['delete'])
    def delete_account(self, request):
        user = request.user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'])
    def activities(self, request):
        activities = UserActivity.objects.filter(user=request.user)[:10]
        serializer = UserActivitySerializer(activities, many=True)
        return Response(serializer.data)