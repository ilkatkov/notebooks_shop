from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Product

def index(request):
    latest_products_list = Product.objects.order_by('-id')[:5]
    return render(request, 'products/list.html', {'latest_products_list': latest_products_list})


def detail(request, product_id):
    try:
        product = Product.objects.get(id = product_id)
    except:
        raise Http404("Товар не найден!")
    
    return render(request, 'products/detail.html', {'product': product})