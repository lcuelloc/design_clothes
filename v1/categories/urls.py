from django.urls import path, include

from rest_framework import routers

from v1.categories.administrator.views import AdminCategoryView
from v1.categories.client.views import ClientCategoryListView

router_admin = routers.SimpleRouter()
router_admin.register(r'categories', AdminCategoryView, base_name='category')

urlpatterns = []

urlpatterns += [
    path('client/categories/', ClientCategoryListView.as_view()),
    path('admin/', include(router_admin.urls)),
]
