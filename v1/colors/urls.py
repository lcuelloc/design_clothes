from django.urls import path

from v1.colors.views.color_list import ColorList
from v1.colors.views.product_color_list import ProductColorList

urlpatterns = [
    path("colors/", ColorList.as_view(), name="color_list"),
    path("product-colors/", ProductColorList.as_view(), name="product_color_list"),
]
