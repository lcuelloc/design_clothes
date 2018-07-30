from django.urls import path

from v1.products.views.product_list import ProductList
from v1.products.views.category_product_list import CategoryProductList
from v1.products.views.product_type_list import ProductTypeList

urlpatterns = [
    path("products/", ProductList.as_view(), name="product_list"),
    path(
        "category-products/",
        CategoryProductList.as_view(),
        name="category_product_list",
    ),
    path("product-types/", ProductTypeList.as_view(), name="product_type_list"),
]
