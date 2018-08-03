from django.urls import path, include

from rest_framework import routers

from v1.tags.views.tag import AdminTagView

router_admin = routers.SimpleRouter()
router_admin.register(r'tags', AdminTagView, base_name='tag')

urlpatterns = []

urlpatterns += [
    path('admin/', include(router_admin.urls)),
]
