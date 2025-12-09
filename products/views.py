from rest_framework import viewsets, permissions
from rest_framework import filters as drf_filters
import django_filters

from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from .permissions import IsOwnerOrReadOnly



# Create your views here.
class ProductFilter(django_filters.FilterSet):

    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte")

    class Meta:
        model = Product
        fields = ["category", "is_active", "min_price", "max_price"]




class CategoryViewSet(viewsets.ModelViewSet):
    
    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class ProductViewSet(viewsets.ModelViewSet):
    
    queryset = Product.objects.all().order_by("-created_at")
    serializer_class = ProductSerializer
    permission_classes = [IsOwnerOrReadOnly]
   

    filter_backends = [
        drf_filters.SearchFilter,
        drf_filters.OrderingFilter,
        DjangoFilterBackend,
    ]


    search_fields = ["name", "description", "stock_quantity"]
    filterset_fields = ["category", "is_active"]
    ordering_fields = ["price", "created_at","stock_quantity"]
    filterset_class = ProductFilter


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


