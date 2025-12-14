from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product
from shipping.models import ShippingAddress
# Create your models here.

User = get_user_model()

class Order(models.Model):
    STATUS_CHOICES = [("PENDING", "Pending"),("PAID", "Paid"),("SHIPPED", "Shipped"),("DELIVERED", "Delivered"),("CANCELLED", "Cancelled"),]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    address = models.ForeignKey(ShippingAddress, on_delete=models.SET_NULL, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="PENDING",db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def calculate_total(self):
        total = sum(
        item.quantity * item.price_at_purchase
        for item in self.items.all())
        self.total_amount = total
        self.save(update_fields=["total_amount"])


    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        indexes = [models.Index(fields=["order"]),]

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
