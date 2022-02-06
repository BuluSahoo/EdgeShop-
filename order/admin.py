from django.contrib import admin, messages
from django.contrib.admin.decorators import action
from order.models import Order, Order_details

# Register your models here.


admin.site.register(Order_details)

def Mark_As_Pending(modeladmin, request, queryset):
    queryset.update(order_status='Pending')
    messages.success(request, 'selected record(s) marked as pending')

def Mark_As_Cancelled(modeladmin, request, queryset):
    queryset.update(order_status='Cancelled')
    messages.error(request, 'selected record(s) marked as Cancelled')

def Mark_As_Delivered(modeladmin, request, queryset):
    queryset.update(order_status='Delivered')
    messages.success(request, 'selected record(s) marked as delivered')

def Mark_As_Inprogress(modeladmin, request, queryset):
    queryset.update(order_status='Inprogress')
    messages.success(request, 'selected record(s) marked as Inprogress')


# class OrderDetailsInline(admin.StackedInline):
class OrderDetailsInline(admin.TabularInline):

    model = Order_details
    extra = 1


class OrderAdmin(admin.ModelAdmin) :
    list_display = ['user','name','date_time','order_status','payment_status']
    list_filter = ['order_status', 'payment_status']
    date_hierarchy = 'date_time'
    actions = [Mark_As_Pending, Mark_As_Cancelled, Mark_As_Delivered, Mark_As_Inprogress]
    inlines= [OrderDetailsInline]

admin.site.register(Order, OrderAdmin)

