from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib import messages
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.contrib import auth
from Utils.local_text import sendSMS
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def home(request):
    context = {'form':contactUsForm}
    return render(request, 'home.html', context)

def contactus(request):
    if request.method == 'POST':
        form = contactUsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            mobile = form.cleaned_data['mobile']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            model = contact_us(name=name, mobile=mobile, email=email, subject=subject, message=message)
            model.save()
            #Sending mess-age to Admin
            # try:
            #     apikey = 'wiNtwACDA3E-FYv4zKVBwOU189WW5cJXpvZk2x2DRG'
            #     admin_mobile = ""
            #     message_to_admin = "Request from customer. Subject: "+subject+" message: "+message
            #     resp =  sendSMS(apikey, admin_mobile,'', message_to_admin)
            # except Exception as e:
            #     messages.warning(request, "Unable to send message. Please try again.")

            #Sending mail to Admin
            #try:
            html_message = render_to_string('email_template.html',{'name':name, 'mobile':mobile, 'email':email, 'message':message})
            email_subject = "Request from "+name+" : "+subject
            admin_email = "tfreshup2@gmail.com"
            mail = EmailMultiAlternatives(email_subject, message, 'sreesai.techservices@gmail.com',  [admin_email,])
            mail.attach_alternative(html_message, "text/html")
            mail.send()
            messages.success(request, "Request has been submitted successfully.")
            messages.success(request, "Our person will contact soon.")
            # except Exception as e:
            #     print("CCTV ERROR : "+str(e))
            #     messages.warning(request, "Unable to send mail. Please try again")
            return HttpResponseRedirect('/#contact')
        else:
            messages.warning(request, "Form is not valid")
            return HttpResponseRedirect("/#contact")
    else:
        return HttpResponseRedirect('/#contact')
