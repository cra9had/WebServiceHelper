from django.urls import path
from .views import RegisterPageView, RegisterAPIView

urlpatterns = [
    path("registerPage", RegisterPageView.as_view()),
    path("register", RegisterAPIView.as_view())
]
