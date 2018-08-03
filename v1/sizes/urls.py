from django.urls import path, include

from rest_framework import routers

from v1.sizes.views.size import AdminSizeView
from v1.sizes.views.product_size import AdminProductSizeView

router_admin = routers.SimpleRouter()
router_admin.register(r'sizes', AdminSizeView, base_name='size')
router_admin.register(r'product-sizes', AdminProductSizeView, base_name='product-size')

urlpatterns = []

urlpatterns += [
    path('admin/', include(router_admin.urls)),
]
