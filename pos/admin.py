from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Employee, Category, Product, CartItem, Transaction

# Register your models here.
admin.site.register(Employee, UserAdmin)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Transaction)