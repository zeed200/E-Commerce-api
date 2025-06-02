from django.urls import path
from .views import RegisterWithGoogleView, LoginAPIView

urlpatterns = [
    path("api/register/", RegisterWithGoogleView.as_view(), name="register_with_google"),
    path("api/login/", LoginAPIView.as_view(), name="login"),
]
