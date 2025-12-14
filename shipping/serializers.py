from rest_framework import serializers
from .models import ShippingAddress

class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = [
            "id",
            "address_line1",
            "city",
            "state",
            "country",
            "phone_number",
            "created_at",
        ]
