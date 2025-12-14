from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cart.models import Cart
from .models import Order, OrderItem

# Create your views here.

class CreateOrderView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        cart = Cart.objects.filter(user=request.user).first()

        if not cart or not cart.items.exists():
            return Response({"error": "Cart is empty"},status=status.HTTP_400_BAD_REQUEST)

        address_id = request.data.get("address_id")

        order = Order.objects.create(user=request.user,address_id=address_id)

        for item in cart.items.select_related("product"):
            OrderItem.objects.create(order=order,product=item.product,quantity=item.quantity,price_at_purchase=item.product.price)

        order.calculate_total()
        cart.items.all().delete()

        return Response({"message": "Order created", "order_id": order.id},status=status.HTTP_201_CREATED)
