from django import forms

class loginForm(forms.Form):
    username = forms.CharField(max_length=15)
    password = forms.CharField(max_length=15)

    def __init__(self, *args, **kwargs):
        super(loginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = "Username"
        self.fields['password'].widget.attrs['placeholder'] = "Password"
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'field-control'

class signupForm(forms.Form):
    """docstring for signupForm."""
    name = forms.CharField(max_length=15)
    username = forms.CharField(max_length=15)
    mobile = forms.CharField(max_length=10)
    email = forms.CharField(max_length=15)
    password = forms.CharField(max_length=15)
    confirm_password = forms.CharField(max_length=15)
    def __init__(self, *args, **kwargs):
        super(signupForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = "Name"
        self.fields['username'].widget.attrs['placeholder'] = "Username"
        self.fields['mobile'].widget.attrs['placeholder'] = "Mobile"
        self.fields['email'].widget.attrs['placeholder'] = "Email"
        self.fields['password'].widget.attrs['placeholder'] = "Password"
        self.fields['confirm_password'].widget.attrs['placeholder'] = "Confirm Password"
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'field-control'

class forgotpassowrd_otpForm(forms.Form):
    otp = forms.CharField(max_length=6, label="OTP")

    def __init__(self, *args, **kwargs):
        super(forgotpassowrd_otpForm, self).__init__(*args, **kwargs)
        self.fields['otp'].widget.attrs['placeholder'] = "Enter OTP"
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'field-control'

class forgotpassword_updateForm(forms.Form):
    new_password = forms.CharField(max_length=15)
    confirm_password = forms.CharField(max_length=15)

    def __init__(self, *args, **kwargs):
        super(forgotpassword_updateForm, self).__init__(*args, **kwargs)
        self.fields['new_password'].widget.attrs['placeholder'] = "New Password"
        self.fields['confirm_password'].widget.attrs['placeholder'] = "Confirm Password"
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'field-control'
