from django.db import models
from products.models import Product


# Create your models here.
class Inventory(models.Model):
    """ track of how many units are in stock."""
    
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="inventory")
    stock_quantity = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} - {self.stock_quantity} in stock"