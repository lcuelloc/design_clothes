from django.urls import path, include

from rest_framework import routers

from v1.locations.views.location import AdminLocationView


router_admin = routers.SimpleRouter()
router_admin.register(r'locations', AdminLocationView, base_name='location')

urlpatterns = []

urlpatterns += [
    path('admin/', include(router_admin.urls)),
]
