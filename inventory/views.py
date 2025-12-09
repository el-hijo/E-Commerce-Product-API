from rest_framework import viewsets, permissions
from .models import Inventory
from .serializers import InventorySerializer
from .permissions import IsProductOwnerOrReadOnly


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsProductOwnerOrReadOnly
    ]

