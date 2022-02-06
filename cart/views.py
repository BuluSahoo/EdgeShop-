from itertools import product
from django.shortcuts import redirect
from django.views import View
from cart.models import Cart

# Create your views here.

class AddToCart(View):
    
    def post(self, request):
        quantity = request.POST.get('quantity')
        product_id = request.POST.get('product_id')

        Cart.objects.create(
            quantity=quantity,
            product_id=product_id,
            user=request.user,
        )
        return redirect('ProductDetails', product_id=product_id)