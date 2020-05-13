from django.urls import path
from products.views import ProductListFBV, ProductListCBV,ProductDetailFBV, ProductDetailCBV

app_name = 'products' #with include

urlpatterns = [
    path('products/fbv/', ProductListFBV, name='Product-ListFBV'), #ProductList is the view to be imported, funciton name
    path('products/cbv/', ProductListCBV.as_view(), name='Product-ListCBV'), 
    path('products/detailfbv/<int:pk>', ProductDetailFBV, name='product-detail-fbv'),
    #pk has to be same parameter going in view function 
    path('products/detailcbv/<int:pk>', ProductDetailCBV.as_view(), name='product-detail-cbv'),

]
