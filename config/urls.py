"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'v1/', include('v1.accounts.urls')),
    path(r'v1/', include('v1.categories.urls')),
    path(r'v1/', include('v1.colors.urls')),
    path(r'v1/', include('v1.sizes.urls')),
    path(r'v1/', include('v1.products.urls')),
    path(r'v1/', include('v1.images.urls')),
    path(r'v1/', include('v1.statics.urls')),
    path(r'v1/', include('v1.prints.urls')),
    path(r'v1/', include('v1.tags.urls')),
    path(r'v1/', include('v1.designs.urls')),
    path(r'v1/', include('v1.locations.urls')),
]
