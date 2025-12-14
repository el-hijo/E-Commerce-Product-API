from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            "id",
            "order",
            "amount",
            "payment_method",
            "transaction_ref",
            "status",
            "created_at",
        ]
        read_only_fields = ["status", "transaction_ref", "created_at"]
