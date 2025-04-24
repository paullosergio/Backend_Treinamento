from django.urls import path
from .views import UserRegistrationView, LoginView, CurrentUser

app_name = "usuarios"

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="user-register"),
    path("login/", LoginView.as_view(), name="user-login"),
    path("current-user/", CurrentUser.as_view(), name="current-user"),
]
