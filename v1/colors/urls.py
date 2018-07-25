from django.urls import path

from v1.colors.views.color_list import ColorList

urlpatterns = [path("colors/", ColorList.as_view(), name="color_list")]
