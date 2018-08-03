from django.urls import path, include

from rest_framework import routers

from v1.categories.views.category import AdminCategoryView

router_admin = routers.SimpleRouter()
router_admin.register(r'categories', AdminCategoryView, base_name='category')

urlpatterns = []

urlpatterns += [
    path('admin/', include(router_admin.urls)),
]
