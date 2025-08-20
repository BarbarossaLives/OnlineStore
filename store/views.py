from django.shortcuts import render
from django.http import JsonResponse
from .models import Product

def home(request):
    """Home page view"""
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

def api_products(request):
    """API endpoint for products"""
    products = Product.objects.all()
    data = []
    for product in products:
        data.append({
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': float(product.price),
            'image': product.image or 'https://via.placeholder.com/300x300',
        })
    return JsonResponse({'products': data})
