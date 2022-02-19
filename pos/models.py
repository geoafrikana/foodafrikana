from django.db import models
from django.contrib.auth.models import AbstractUser

class Employee(AbstractUser):
    class Meta:
        verbose_name = "Employee"
    def __str__(self):
        return self.username

class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    cat_name = models.CharField(max_length=50)

    def __str__(self):
        return self.cat_name


class Product(models.Model):
    prod_name = models.CharField(max_length= 50)
    prod_cat = models.ForeignKey(Category, related_name="products_cat", on_delete=models.CASCADE)
    prod_cost = models.IntegerField()

    class Meta:
        verbose_name = "Food Item"
    
    def __str__(self):
        return self.prod_name

class CartItem(models.Model):
    item_prod = models.ForeignKey(Product,  related_name="carts", on_delete=models.CASCADE)
    item_quantity = models.IntegerField(default=1)


class Transaction(models.Model):
    trans_items = models.ForeignKey(CartItem, related_name="transaction", on_delete=models.CASCADE)
    trans_date = models.DateTimeField(auto_now_add = True)
    trans_seller = models.ForeignKey(Employee, related_name="sales", on_delete=models.CASCADE)
