from django.urls import path, include

from rest_framework import routers

from v1.designs.views.category_design import AdminCategoryDesignView
from v1.designs.views.design import AdminDesignView
from v1.designs.views.upload_design import AdminUploadDesignView
from v1.designs.client.views import ClientDesignListView
from v1.designs.client.views import ClientCategoryDesignListView

router_admin = routers.SimpleRouter()
router_admin.register(r'category-designs', AdminCategoryDesignView, base_name='category-design')
router_admin.register(r'designs', AdminDesignView, base_name='design')

urlpatterns = []

urlpatterns += [
    path("admin/upload-designs/", AdminUploadDesignView.as_view()),
    path('client/designs/', ClientDesignListView.as_view()),
    path('client/category-designs/', ClientCategoryDesignListView.as_view()),
    path('admin/', include(router_admin.urls)),
]
