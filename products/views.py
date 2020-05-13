from django.shortcuts import render
from .models import Product
from django.views.generic import ListView, DetailView

# def HelloDjango(request):
#     name = "Sona"
#     last_name = "Sharma"
#     context = {
#         'first_name': name,
#         'last_name': last_name
#     }

#     return render(request, 'products/hello-django.html', context)

def ProductListFBV(request):
    #product_list = Product.objects.all()
    product_list = Product.objects.filter(price__lt=16)
    #u can call this map anything,
    context={
        'product_list' : product_list
    }
    return render(request, 'products/product-list.html', context) #can call context anything or dict

class ProductListCBV(ListView):
    model = Product
    #queryset = Product.objects.filter(price__lt=11)
    context_object_name='product_list'
    template_name= 'products/product-list.html'

def ProductDetailFBV(request, pk):
    #product= Product.objects.get(id=pk) #returns product
    product_qs= Product.objects.filter(id=pk) #returns query set or list
    #if empty it will not throw error but throw empty list
    product=product_qs[0]
    context = {
        'product': product
    }
    return render(request, 'products/product-detail.html', context)

class ProductDetailCBV(DetailView):
    model = Product #in list view its a lsit not here  this is the get function not the all function
    context_object_name = 'product'
    template_name = 'products/product-detail.html'