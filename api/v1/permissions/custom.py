from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permissão personalizada para permitir que apenas o proprietário
    de um objeto possa editá-lo.
    """
    
    def has_object_permission(self, request, view, obj):
        # Permissões de leitura para qualquer requisição
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Permissões de escrita apenas para o proprietário do objeto
        return obj.criado_por == request.user


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Permissão que permite acesso apenas ao proprietário ou administradores.
    """
    
    def has_object_permission(self, request, view, obj):
        # Administradores têm acesso total
        if request.user.is_staff:
            return True
        
        # Proprietário tem acesso total
        if hasattr(obj, 'criado_por'):
            return obj.criado_por == request.user
        elif hasattr(obj, 'user'):
            return obj.user == request.user
        
        return False


class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    """
    Permissão que permite leitura para todos, mas escrita apenas para usuários autenticados.
    """
    
    def has_permission(self, request, view):
        # Permissões de leitura para qualquer requisição
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Permissões de escrita apenas para usuários autenticados
        return request.user and request.user.is_authenticated


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permissão que permite leitura para todos, mas escrita apenas para administradores.
    """
    
    def has_permission(self, request, view):
        # Permissões de leitura para qualquer requisição
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Permissões de escrita apenas para administradores
        return request.user and request.user.is_staff


class IsOwnerOrAdminOrReadOnly(permissions.BasePermission):
    """
    Permissão que permite:
    - Leitura para todos
    - Escrita para o proprietário ou administradores
    """
    
    def has_permission(self, request, view):
        # Permissões de leitura para qualquer requisição
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Permissões de escrita apenas para usuários autenticados
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        # Permissões de leitura para qualquer requisição
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Administradores têm acesso total
        if request.user.is_staff:
            return True
        
        # Proprietário tem acesso total
        if hasattr(obj, 'criado_por'):
            return obj.criado_por == request.user
        elif hasattr(obj, 'user'):
            return obj.user == request.user
        
        return False

