from django.urls import path
from . import views

app_name = "accounturls"

urlpatterns = [
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('forgotpassword/', views.forgotpassword, name="forgotpassword"),
]
