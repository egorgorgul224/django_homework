from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView, email_verification

app_name = "users"

urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="catalog:product_list_home"), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("email-confirm/<str:token>/", email_verification, name="email-confirm"),
]
