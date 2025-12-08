from rest_framework import viewsets, permissions, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from .permissions import IsOwnerOrReadOnly



# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    """API endpoint for managing product categories."""
    
    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class ProductViewSet(viewsets.ModelViewSet):
    """API endpoint for managing products."""
    
    queryset = Product.objects.all().order_by("-created_at")
    serializer_class = ProductSerializer
    permission_classes = [IsOwnerOrReadOnly]
   

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]


    search_fields = ["name", "description", "stock_quantity"]

    filterset_fields = ["category", "is_active"]

    ordering_fields = ["price", "created_at","stock_quantity"]

    def perform_create(self, serializer):
        """Assigns the product owner to the logged-in user."""
        serializer.save(owner=self.request.user)
