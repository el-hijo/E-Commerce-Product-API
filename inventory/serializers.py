from rest_framework import serializers
from .models import Inventory


class InventorySerializer(serializers.ModelSerializer):
    """Serializer for inventory records."""

    product_name = serializers.CharField(
        source="product.name",
        read_only=True,
        help_text="Name of the product this inventory belongs to."
    )

    class Meta:
        model = Inventory
        fields = [
            "id",
            "product",
            "product_name",
            "stock_quantity",
            "updated_at",
        ]
        read_only_fields = ["id", "updated_at", "product_name"]
