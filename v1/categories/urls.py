from django.urls import path

from v1.categories.views.category_list import CategoryList

urlpatterns = [path("categories/", CategoryList.as_view(), name="category_list")]
