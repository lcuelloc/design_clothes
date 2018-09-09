from django.urls import path, include

from rest_framework import routers

from v1.products.views.product import AdminProductView

router_admin = routers.SimpleRouter()
router_admin.register(r"products", AdminProductView, base_name="product")

urlpatterns = []

urlpatterns += [path("admin/", include(router_admin.urls))]
