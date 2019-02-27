from django.shortcuts import render
from .forms import *
# Create your views here.

def login(request):
    return render(request, 'accounts/login.html', {"form": loginForm()})

def signup(request):
    return render(request, 'accounts/signup.html', {"form": signupForm()})

def forgotpassword(request):
    otp_generated = True
    return render(request, 'accounts/forgotpassword.html', {"otpform": forgotpassowrd_otpForm(),
                                                            "updateform":forgotpassword_updateForm(),
                                                            "otp_generated":otp_generated})
