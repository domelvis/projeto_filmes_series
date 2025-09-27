# API permissions package
from .custom import (
    IsOwnerOrReadOnly,
    IsOwnerOrAdmin,
    IsAuthenticatedOrReadOnly,
    IsAdminOrReadOnly,
    IsOwnerOrAdminOrReadOnly,
)

__all__ = [
    'IsOwnerOrReadOnly',
    'IsOwnerOrAdmin',
    'IsAuthenticatedOrReadOnly',
    'IsAdminOrReadOnly',
    'IsOwnerOrAdminOrReadOnly',
]
