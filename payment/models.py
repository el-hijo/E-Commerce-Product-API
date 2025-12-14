from django.db import models
from order.models import Order
# Create your models here.

class Payment(models.Model):
    STATUS_CHOICES = [("PENDING", "Pending"),("SUCCESS", "Success"),("FAILED", "Failed"),]

    order = models.OneToOneField(Order,on_delete=models.CASCADE,related_name="payment")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="PENDING")
    payment_method = models.CharField(max_length=50) 
    transaction_ref = models.CharField(max_length=255, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.transaction_ref} - {self.status}"
