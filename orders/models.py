from django.db import models

from goods.models import Product
from users.models import User

# Create your models here.

class OrderitemQueryset(models.QuerySet):

 def total_price(self):
        return sum(cart.product_price() for cart in self)

def total_quantity(self):
    if self:
        return sum(cart.quantity for cart in self)
    return 0


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, blank=True, null=True, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=20)
    requires_delivery = models.BooleanField(default=False)
    delivery_addres = models.TextField(null=True, blank=True)
    peyment_on_get = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    status = models.CharField(max_length=50, default="In process")

    class Meta:
        db_table = "Order"

    def __str__(self):
        return f"Order №{self.pk} | User {self.user.first_name} {self.user.last_name}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_DEFAULT, null=True, default=None)
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "order_item"

    objects = OrderitemQueryset.as_manager()

    def products_price(self):
        return round(self.product.price_sale() * self.quantity, 2)
    
    def __str__(self):
        return f"Product {self.name} | Order №{self.order.pk}"