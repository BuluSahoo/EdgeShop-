from os import name
from django import views
from django.urls import path
from . import views
urlpatterns =[
    path('', views.HomePage.as_view(), name="HomePage"),
    path('product-listing/<int:ProductCategory_id>',views.ProductListing.as_view(),name="ProductListing"),
    path('product-details/<int:Product_id>',views.ProductDetails.as_view(),name="ProductDetails"),
    
]