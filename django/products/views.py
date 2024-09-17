from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Product


def index(request):
    try:
        products = Product.objects.all()
        return render(request, 'index.html', {'products' : products})
    except Product.DoesNotExist:
        raise Http404('Product Does not exist')
    except:
        raise Http404('Page does not exist')
    

def details(request, product_id):
    try:
        product_details = Product.objects.get(id=product_id)
        return render(request, 'details.html', {'product_details': product_details})
    except Product.DoesNotExist:
        raise Http404('product does not exist')