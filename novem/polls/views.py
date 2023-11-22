from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def product_list(request):
    products = Product.objects.all().order_by('price')
    return render(request, 'product_list.html', {'products': products})
