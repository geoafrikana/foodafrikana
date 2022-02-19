from rest_framework import serializers
from .models import Employee, Product, Category


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ["url", 'prod_name', 'prod_cat', 'prod_cost']

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ["url", "cat_name"]


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ["url", "username", "email", "first_name", "last_name"]