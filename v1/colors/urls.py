from django.urls import path, include

from rest_framework import routers

from v1.colors.views.color import AdminColorView
from v1.colors.views.product_color import AdminProductColorView

router_admin = routers.SimpleRouter()
router_admin.register(r'colors', AdminColorView, base_name='color')
router_admin.register(r'product-colors', AdminProductColorView, base_name='product-colors')

urlpatterns = []

urlpatterns += [
    path('admin/', include(router_admin.urls)),
]
