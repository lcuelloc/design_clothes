from django.urls import path, include

from rest_framework import routers

from v1.designs.views.category_design import AdminCategoryDesignView

router_admin = routers.SimpleRouter()
router_admin.register(r'category-designs', AdminCategoryDesignView, base_name='category-design')

urlpatterns = []

urlpatterns += [
    path('admin/', include(router_admin.urls)),
]
