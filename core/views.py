from django.shortcuts import render, redirect
from django.http import Http404
from core.models import User, Product
from django.db.models import Count
from django.contrib import messages



def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {
        'products': products,
    })

def relaunch(request):
    products = Product.objects.all()
    return render(request, 'relaunch.html', {
        'products': products,
    })

def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'product_detail.html', {
        'product': product,
    })

