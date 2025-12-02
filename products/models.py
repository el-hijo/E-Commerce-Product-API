from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Category(models.Model):
    """
    Represents the category of products.
    Example: Diary, Canned Foods, Toileteries etc.
    """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    """Represents available product. Contains product's 
    attributes like: name, description, price, stock quantity etc."""
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock_quantity = models.PositiveBigIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    image = models.URLField(max_length=500, blank=True, null=True) 
    created_at =models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,
                                 related_name="products")
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name="products")   
    
    class Meta:
        ordering =['-created_at']
        
    def __str__(self):
        return self.name