from django.urls import path

from v1.accounts.views.registration import RegistrationView
from v1.accounts.views.login import JWTLoginView


urlpatterns = [
    path('auth-token/', JWTLoginView.as_view(), name='login'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    ]
