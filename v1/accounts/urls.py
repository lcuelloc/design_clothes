from django.urls import path, include

from rest_framework import routers

from v1.accounts.views.registration import RegistrationView
from v1.accounts.views.login import JWTLoginView
from v1.accounts.views.user import AdminUserView


router_admin = routers.SimpleRouter()
router_admin.register(r'users', AdminUserView, base_name='user')

urlpatterns = [
    path("auth-token/", JWTLoginView.as_view(), name="login"),
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("admin/", include(router_admin.urls)),
]
