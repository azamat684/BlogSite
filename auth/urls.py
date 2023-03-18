from django.urls import path
from .views import LoginUserAPIView, LogOutUserAPIView, RegisterUserAPIView


urlpatterns = [
    path("register/", RegisterUserAPIView.as_view(), name="register"),
    path('login/', LoginUserAPIView.as_view(), name="login"),
    path('logout/', LogOutUserAPIView.as_view(), name="logout"),
]
