from django.urls import path

from v1.sizes.views.size_list import SizeList
from v1.sizes.views.product_size_list import ProductSizeList

urlpatterns = [
    path("sizes/", SizeList.as_view(), name="size_list"),
    path("product-sizes/", ProductSizeList.as_view(), name="product_size_list"),
]
