from django.urls import path, include

from rest_framework import routers

from v1.prints.views.print import AdminPrintView
from v1.prints.views.print_product import AdminPrintProductView

router_admin = routers.SimpleRouter()
router_admin.register(r'prints', AdminPrintView, base_name='print')
router_admin.register(r'print-products', AdminPrintProductView, base_name='print-products')

urlpatterns = []

urlpatterns += [
    path('admin/', include(router_admin.urls)),
]