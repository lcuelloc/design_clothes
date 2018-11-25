from django.urls import path, include

from rest_framework import routers

from v1.locations.administrator.views import AdminLocationView
from v1.locations.client.views import ClientLocationView


router_admin = routers.SimpleRouter()
router_admin.register(r'locations', AdminLocationView, base_name='location')

router_client = routers.SimpleRouter()
router_client.register(r'locations', ClientLocationView, base_name='location')

urlpatterns = []

urlpatterns += [
    path('admin/', include(router_admin.urls)),
    path('client/', include(router_admin.urls)),
]
