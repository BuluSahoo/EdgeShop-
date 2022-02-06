from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey

# Create your models here.
class ProductCategory(models.Model):
    '''Productcategory model'''
    name = models.CharField(max_length=150)
    status = models.BooleanField(default=True)

    def __str__(self):
        '''string representation for object Productcategory object(1) '''
        return str(self.name)


class Product (models.Model):
    ''' product model'''
    ProductCategory = ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name="ProductCategory")
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField(default=1)
    cover_image = models.ImageField()
    status = models.BooleanField(default=True)

    def __str__(self) :
        return str(self.name)


class ProductImage(models.Model):
    ''' product will have more than one images'''
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self) :
        return str(self.Product)