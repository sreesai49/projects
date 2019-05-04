from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib import messages
from django.http import Http4
# Create your views here.

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid() and form.cleaned_data['password']==form.cleaned_data['confirm_password']:
            model = user_registration()
            model.first_name = form.cleaned_data['first_name']
            model.last_name = form.cleaned_data['last_name']
            model.username = form.cleaned_data['username']
            model.mobile = form.cleaned_data['mobile']
            model.email = form.cleaned_data['email']
            model.password = form.cleaned_data['password']
            model.save()
            user_login(user=model, username=form.cleaned_data['username'], email=form.cleaned_data['email'], password=form.cleaned_data['password']).save()
            form = registerForm()
            messages.success(request, "Registration has been completed successfully.")
        elif form.cleaned_data['password'] != form.cleaned_data['confirm_password']:
            form.add_error('confirm_password', 'The passwords do not match')
        else:
            raise Http4

    else:
        form = registerForm()
    return render(request, 'register.html', {"table_form": form.as_table()})

def login(request):
    pass
