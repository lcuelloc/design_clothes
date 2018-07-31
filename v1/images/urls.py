from django.urls import path

from v1.images.views.image_list import ImageList

urlpatterns = [
    path("images/", ImageList.as_view(), name="image_list"),
]
