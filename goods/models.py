from pyexpat import model
from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"
    


class Product(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='goods_images', blank=True, null=True)
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)
        
    def __str__(self):
        return f"{self.name} {self.quantity}"
    
    def get_absolute_url(self):
        return reverse("catalog:product" , kwargs={"product_slug": self.slug})
    
    
    def show_id(self):
        return f"{self.id:05}"
    
    def price_sale(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price