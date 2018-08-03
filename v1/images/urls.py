from django.urls import path, include

from rest_framework import routers

from v1.images.views.image import AdminImageView

router_admin = routers.SimpleRouter()
router_admin.register(r'images', AdminImageView, base_name='image')

urlpatterns = []

urlpatterns += [
    path('admin/', include(router_admin.urls)),
]