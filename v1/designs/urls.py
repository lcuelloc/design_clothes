from django.urls import path, include

from rest_framework import routers

from v1.designs.views.category_design import AdminCategoryDesignView
from v1.designs.views.design import AdminDesignView

router_admin = routers.SimpleRouter()
router_admin.register(r'category-designs', AdminCategoryDesignView, base_name='category-design')
router_admin.register(r'designs', AdminDesignView, base_name='design')

urlpatterns = []

urlpatterns += [
    path('admin/', include(router_admin.urls)),
]
