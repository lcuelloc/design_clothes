from django.urls import path, include

from rest_framework import routers

from v1.products.views.product import AdminProductView
from v1.products.views.upload_product import AdminUploadProductView

router_admin = routers.SimpleRouter()
router_admin.register(r"products", AdminProductView, base_name="product")

urlpatterns = []

urlpatterns += [
    path("admin/upload-products/", AdminUploadProductView.as_view()),
    path("admin/", include(router_admin.urls)),
]
