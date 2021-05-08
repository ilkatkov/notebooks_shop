from django.shortcuts import render
from .models import Product

def index(request):
    latest_products_list = Product.objects.order_by('-id')[:5]
    return render(request, 'products/list.html', {'latest_products_list': latest_products_list})