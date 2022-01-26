from django.urls import path
from .views import RegisterPageView, RegisterAPIView


urlpatterns = [
	path("register/<str:url_hash>", RegisterPageView.as_view()),
	path("register", RegisterAPIView.as_view())
]
