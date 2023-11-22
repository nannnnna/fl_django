from django.urls import path
from . import views
from .views import product_list

urlpatterns = [
    path("", views.index, name="index"),
    path('products/', product_list, name='product_list'),
]