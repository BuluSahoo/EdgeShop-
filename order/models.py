from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from product.models import Product

# Create your models here.

class Order(models.Model):
    ''' Order model'''
    order_status_choices =(
        ('Pending', 'Pending'),
        ('Inprogress', 'Inprogress'),
        ('Cancelled', 'Cancelled'),
        ('Delivered', 'Delivered')
    )
    user = models.ForeignKey(User, on_delete= CASCADE)
    date_time =models.DateTimeField()
    name = models.CharField(max_length=150)
    address = models.TextField()
    payment_status = models.BooleanField(default=False)
    order_status = models.CharField(max_length=255, choices=order_status_choices, default='Pending')

    def __str__(self) :
        return str(self.id)


class Order_details(models.Model):
    order = models.ForeignKey(Order, on_delete=CASCADE)
    product =models.ForeignKey(Product, on_delete=CASCADE)
    quantity = models.IntegerField()
    product_price =models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self) :
        return f'{self.order.id} - {self.product}'