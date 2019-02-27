from django.urls import path
from . import views

app_name = "homeurls"

urlpatterns = [
    path('', views.home, name="home"),
    path('aboutus', views.aboutus, name="aboutus"),
]
