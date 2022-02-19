from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ProductSerializer, CategorySerializer, EmployeeSerializer
from .models import Product, Category, Employee


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('prod_cat')
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [permissions.IsAuthenticated]

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # permission_classes = [permissions.IsAuthenticated]

