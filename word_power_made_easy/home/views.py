from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home/homepage.html')

def aboutus(request):
    with open('Static/content/aboutus.txt') as about_text:
        text = about_text.read()
    return render(request, 'home/aboutus.html', {"aboutus_content": text})
