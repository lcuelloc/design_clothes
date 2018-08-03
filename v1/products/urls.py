from django.urls import path, include

from rest_framework import routers

from v1.products.views.category_product import AdminCategoryProductView
from v1.products.views.product import AdminProductView
from v1.products.views.product_type import AdminProductTypeView

router_admin = routers.SimpleRouter()
router_admin.register(
    r"category-products", AdminCategoryProductView, base_name="category-product"
)
router_admin.register(r"products", AdminCategoryProductView, base_name="product")
router_admin.register(
    r"product-types", AdminCategoryProductView, base_name="product-type"
)

urlpatterns = []

urlpatterns += [path("admin/", include(router_admin.urls))]
