from django.http import HttpResponse
from django.shortcuts import render
from .forms import *

def home(request):
    context = {'form':contactUsForm}
    return render(request, 'home.html', context)
