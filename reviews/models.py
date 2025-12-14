from django.db import models
from django.contrib.auth import get_user_model
from products.models import Produc
# Create your models here.

User = get_user_model()

class Review(models.Model):
    RATING_CHOICES = [(1, "Very Bad"),(2, "Bad"),(3, "Okay"),(4, "Good"),(5, "Excellent"),]

    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="reviews")
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="reviews")
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    comment = models.TextField(blank=True)
    is_approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "product")
        indexes = [models.Index(fields=["product"]),]

    def __str__(self):
        return f"{self.user.username} - {self.product.name} ({self.rating})"


