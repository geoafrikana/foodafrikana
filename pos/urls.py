from django.urls import  path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'product', views.ProductViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'employee', views.EmployeeViewSet)


urlpatterns = [
    # path('', include(router.urls)),
    path('api/', include(router.urls) )
]