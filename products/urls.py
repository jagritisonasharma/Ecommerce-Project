from django.urls import path
from products.views import HelloDjango

app_name = 'products' #with include

urlpatterns = [
    path('products-list', HelloDjango, name='hello-world'),
]
