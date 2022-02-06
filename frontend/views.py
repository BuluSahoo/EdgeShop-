from itertools import product
from re import template
from telnetlib import STATUS
from django import views
from django.http import request
from django.shortcuts import render
from django.views import View
from product.models import ProductCategory, Product, ProductImage
# Create your views here.

class HomePage(View):
    def get(self, request):
        navigationProductCategories = ProductCategory.objects.filter(status=True)
        # productCategories = ProductCategory.objects.filter(status=True).order_by('-id')[:4]
        productCategories = ProductCategory.objects.filter(status=True)

        for productCategory in productCategories :
            print(productCategory.ProductCategory.filter(status=True))

        context = {
            'navigationProductCategories' : navigationProductCategories,
            'productCategories' : productCategories

        }  
        
        return render(request, 'home_page.html', context)


class ProductListing(View):

    template_name = 'product-listing.html'

    def get(self,request,ProductCategory_id):
        navigationProductCategories = ProductCategory.objects.filter(status=True,)
        products = Product.objects.filter(status=True,ProductCategory_id=ProductCategory_id)
        context ={
            'navigationProductCategories' : navigationProductCategories,
            'products' : products,
            'ProductCategory_id' : ProductCategory_id
        }

        return render(request, self.template_name, context)


class ProductDetails(View):
    template_name = 'product-details.html'


    def get(self,request, Product_id):
        navigationProductCategories = ProductCategory.objects.filter(status=True,)       
        try:
            product= Product.objects.get(pk=Product_id)
            relatedProducts = Product.objects.filter(status=True, ProductCategory_id=product.ProductCategory_id).exclude(id=Product_id)
        except Product.DoesNotExist:
            product ={}
            relatedProducts = {}

        productImages= ProductImage.objects.filter(Product_id=Product_id)
        context ={
            'navigationProductCategories' : navigationProductCategories,
            'product' : product,
            'productImages': productImages,
            'relatedProducts': relatedProducts
        }
        return render(request, self.template_name, context)

   