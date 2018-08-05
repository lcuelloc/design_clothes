from django.urls import path, include

from rest_framework import routers

from v1.tags.views.tag import AdminTagView
from v1.tags.views.tag_design import AdminTagDesignView

router_admin = routers.SimpleRouter()
router_admin.register(r'tags', AdminTagView, base_name='tag')
router_admin.register(r'tag-designs', AdminTagDesignView, base_name='tag-design')

urlpatterns = []

urlpatterns += [
    path('admin/', include(router_admin.urls)),
]
