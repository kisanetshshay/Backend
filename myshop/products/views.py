
from django.shortcuts import render, get_object_or_404
from .models import Product
import os
from django.conf import settings

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
   
    print("Template DIRS:", settings.TEMPLATES[0]['DIRS'])
    print("BASE_DIR:", settings.BASE_DIR)
    print("Does template exist?", os.path.exists(os.path.join(settings.BASE_DIR, 'templates/products/product_detail.html')))
    
    return render(request, 'products/product_detail.html', {'product': product})
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})