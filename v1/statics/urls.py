from django.urls import path, include

from rest_framework import routers

from v1.statics.views.static import AdminStaicView

router_admin = routers.SimpleRouter()
router_admin.register(r'statics', AdminStaicView, base_name='static')

urlpatterns = []

urlpatterns += [
    path('admin/', include(router_admin.urls)),
]
