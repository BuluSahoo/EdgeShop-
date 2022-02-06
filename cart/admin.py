from django.contrib import admin
from cart.models import Cart

# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ['user','product', 'quantity']
    search_fields = ['product__name']

admin.site.register(Cart, CartAdmin)