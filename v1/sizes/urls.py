from django.urls import path

from v1.sizes.views.size_list import SizeList

urlpatterns = [path("sizes/", SizeList.as_view(), name="size_list")]
