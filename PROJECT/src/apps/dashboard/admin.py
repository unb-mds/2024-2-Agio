from django.contrib import admin
from apps.dashboard.models import UserTable, ProductTable


# Register your models here.

@admin.register(UserTable)
class UserTableAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'name',
                    'email',
                    'password']


@admin.register(ProductTable)
class ProductTableAdmin(admin.ModelAdmin):
    list_display = ['product_name',
                    'amount',
                    'category',
                    'description',
                    'price']
