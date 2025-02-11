from django.contrib import admin
from apps.dashboard.models import *

# Register your models here.

@admin.register(UserTable)
class SeuModeloAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'password'] 

@admin.register(ProductTable)
class SeuModeloAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'amount', 'category', 'description','price'] 
