from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    
    """Serializer for handling category data"""
    class Meta:
        model = Category
        fields = [
            "name",
            "slug",
            "created_at",
        ]
        
        read_only_fields = ["name", "created_at"]
    
    
class ProductSerializer(serializers.ModelSerializer):
    
    """Serializer for handling product data"""
    category_name = serializers.CharField(
        source="category.name",
        read_only=True,
        help_text="Readable name of the product's category",
    )

    owner_username = serializers.CharField(
        source="owner.username",
        read_only=True,
        help_text="Username of the product creator")
    
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "price",
            "sku",
            "category",
            "category_name",
            "stock",
            "is_active",
            "owner",
            "owner_username",
            "created_at",
        ]
        
        read_only_fields = [
            "id",
            "owner",
            "created_at",
            "updated_at",
            "category_name",
            "owner_username",
        ]