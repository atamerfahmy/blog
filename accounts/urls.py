from django.urls import path
from accounts.views import SignUpView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("signup", SignUpView.as_view(), name='accounts.signup'),
    path("logout", LogoutView.as_view(), name='logout'),
]