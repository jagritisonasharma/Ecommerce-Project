from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls', namespace= 'products')), #namespace can be anything to name path but we keep it as app name
]
