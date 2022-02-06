from django.contrib import admin, messages
from django.contrib.admin.decorators import action
from django.contrib.admin.options import TabularInline
from product.models import ProductCategory, Product, ProductImage

# Register your models here.

def activeStatus(modeladmin,request, queryset):
    queryset.update(status=True)
    messages.success(request, 'selected record(s) marked as active')
    # messages.warning(request, 'selected record(s) marked as active')
    # messages.info(request, 'selected record(s) marked as active')
    # messages.debug(request, 'selected record(s) marked as active')


def inactiveStatus(modeladmin,reqest,queryset):
    queryset.update(status=False)
    # messages.error(reqest, 'selected record(s) marked as inactive')
    messages.success(reqest, 'selected record(s) marked as inactive')




def Test(modeladmin,reqest,queryset):
    queryset.update(status=False)

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    list_filter = ('status',)
    search_fields = ('name',)
    actions = (activeStatus, inactiveStatus, Test)
    

admin.site.register(ProductCategory, ProductCategoryAdmin)


# product admin config

class ProductImageAdmin(admin.TabularInline):
    model = ProductImage
    extra = 1
    classes = ('collapse',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','status','stock']
    list_filter = [ 'status']
    search_fields = ['name', 'price']
    actions = [activeStatus, inactiveStatus,]
    inlines = [ProductImageAdmin]

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)

