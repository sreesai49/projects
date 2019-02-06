from django import forms

class contactUsForm(forms.Form):
    name = forms.CharField(max_length=50, label="")
    mobile = forms.CharField(max_length=10, label="")
    email = forms.CharField(max_length=50, label="")
    subject = forms.CharField(max_length=150, label="")
    message = forms.CharField(max_length=250, widget=forms.Textarea, label="")

    def __init__(self, *args, **kwargs):
        super(contactUsForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Full Name*'
        self.fields['mobile'].widget.attrs['placeholder'] = 'Mobile Number*'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['subject'].widget.attrs['placeholder'] = 'Subject*'
        self.fields['message'].widget.attrs['placeholder'] = 'Message*'
        self.fields['message'].widget.attrs['rows'] = '8'
        self.fields['message'].widget.attrs['cols'] = '50'
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'inputs'
