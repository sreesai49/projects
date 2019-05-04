from django import forms
from .models import *
from django.forms import ModelForm

class registerForm(forms.ModelForm):
    """docstring for registerForm."""
    confirm_password = forms.CharField(max_length=15, widget=forms.PasswordInput)
    class Meta:
        model = user_registration
        fields = "__all__"
        widgets = {
            'password': forms.PasswordInput(),
            'confirm_password': forms.PasswordInput(),
        }
    def __init__(self, *args, **kwargs):
        super(registerForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = "Email ID"

class loginForm(forms.ModelForm):
    """docstring for loginForm."""
    class Meta:
        model = user_login
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
