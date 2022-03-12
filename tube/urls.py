from django.urls import path
from .views import MainView
from .views import MyLoginView
from .views import upload_file
from .views import MySignupView

from django.views.generic import RedirectView

app_name = "tube"
urlpatterns = [
    path("", RedirectView.as_view(url="tube/")),
    path("tube/", MainView.as_view(), name="main"),
    path("login/", MyLoginView.as_view(), name="login"),
    path("signup/", MySignupView.as_view(), name="signup"),
    path("/tube/upload/", upload_file, name="upload"),
]
