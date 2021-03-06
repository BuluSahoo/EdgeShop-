from ctypes.wintypes import DWORD
from re import template
from django.shortcuts import render, redirect
from django.urls import is_valid_path
from django.views import View
from product.models import ProductCategory
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as Authlogin, logout as Authlogout
# Create your views here.

class Login(View):

    template_name = 'login.html'
    form_class = AuthenticationForm
    navigationProductCategories = ProductCategory.objects.filter(status=True)
    def get(self, request):
        form = self.form_class()
        context = {
            'navigationProductCategories': self.navigationProductCategories,
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid() :
            Authlogin(request, form.get_user())
            return redirect('HomePage')
        context = {
            'navigationProductCategories': self.navigationProductCategories,
            'form': form,
        }
        return render(request, self.template_name, context)

def logout(request):
    Authlogout(request)
    return redirect('HomePage')


