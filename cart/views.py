from rest_framework import generics, permissions
from .models import Cart, CartItem
from .serializers import CartSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.models import Product
# Create your views here.

class CartDetailView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart



class AddToCartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        product_id = request.data.get("product_id")
        quantity = int(request.data.get("quantity", 1))

        if quantity < 1:
            return Response({"error": "Quantity must be at least 1"},status=status.HTTP_400_BAD_REQUEST)

        product = Product.objects.get(id=product_id)
        cart, _ = Cart.objects.get_or_create(user=request.user)

        cart_item, created = CartItem.objects.get_or_create(cart=cart,product=product)

        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity

        cart_item.save()

        return Response({"message": "Item added to cart"})


class RemoveFromCartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, item_id):
        cart = Cart.objects.get(user=request.user)
        CartItem.objects.filter(cart=cart, id=item_id).delete()
        return Response({"message": "Item removed from cart"})
