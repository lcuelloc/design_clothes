from django.urls import path

from v1.products.views.product_list import ProductList

urlpatterns = [path("products/", ProductList.as_view(), name="product_list")]
