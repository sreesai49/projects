from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib import messages
from django.http import Http404
from django.contrib.auth import login, logout, authenticate
from django.db.models import Q
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
            raise Http404

    else:
        form = registerForm()
    return render(request, 'register.html', {"table_form": form.as_table()})

def login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = user_login.objects.get(Q(username=username) | Q(email=username))
                try:
                    print("Sreesai: Username is verified.")
                    if password == user.password:
                        active_user = authenticate(username = username, password = password)
                        login(request, active_user)
                        return render(request, 'dashbaord/home.html',{'user':user})
                except Exception as e:
                    form.add_error('password', 'Entered wrong password.')
            except Exception as e:
                form.add_error('password', 'User is not found.')
        else:
            raise Http404
    else:
        form = loginForm()

    return render(request, 'login.html', {'form':form})
