from django.urls import path, include

from rest_framework import routers

from v1.prints.views.print_type import AdminPrintTypeView
from v1.prints.views.print_product import AdminPrintProductView

router_admin = routers.SimpleRouter()
router_admin.register(r'print-types', AdminPrintTypeView, base_name='print-type')
router_admin.register(r'print-products', AdminPrintProductView, base_name='print-products')

urlpatterns = []

urlpatterns += [
    path('admin/', include(router_admin.urls)),
]
