from django.urls import path
from . import views

app_name = "registration"

urlpatterns = [
    path('', views.home),
    path('register/', views.register, name="signup"),
    path('login/', views.login, name="signin"),
]
