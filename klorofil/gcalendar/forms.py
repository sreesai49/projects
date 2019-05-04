from django import forms
from django.contrib.admin import widgets

class add_event(forms.Form):
    """docstring for add_event."""
    title = forms.CharField(max_length=35)
    event_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    event_time = forms.TimeField(widget=forms.DateInput(attrs={'placeholder':'HH:MM'}))
    def __init__(self, *args, **kwargs):
        super(add_event, self).__init__(*args, **kwargs)
        self.fields['event_time'].widget = widgets.AdminTimeWidget()

class update_event(forms.Form):
    """docstring for update_event."""
    #Get event
