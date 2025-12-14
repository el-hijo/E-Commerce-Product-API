import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from order.models import Order
from .models import Payment

# Create your views here.


class InitializePaymentView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        order_id = request.data.get("order_id")
        payment_method = request.data.get("payment_method")

        order = Order.objects.get(id=order_id, user=request.user)

        if order.status != "PENDING":
            return Response({"error": "Order already paid or processed"},status=status.HTTP_400_BAD_REQUEST)

        transaction_ref = str(uuid.uuid4())

        payment = Payment.objects.create(order=order,amount=order.total_amount,payment_method=payment_method,transaction_ref=transaction_ref)

        return Response({
            "message": "Payment initialized",
            "transaction_ref": transaction_ref,
            "amount": payment.amount})

class VerifyPaymentView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        transaction_ref = request.data.get("transaction_ref")

        payment = Payment.objects.get(transaction_ref=transaction_ref,order__user=request.user)

        # Simulate successful payment (gateway callback goes here)
        payment.status = "SUCCESS"
        payment.save()

        order = payment.order
        order.status = "PAID"
        order.save()

        return Response({"message": "Payment verified successfully"})
