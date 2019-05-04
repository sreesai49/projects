from django.shortcuts import render
from .forms import *
from .insert_event import ginsert
from .get_events import get_event
from .delete_event import gevent_delete
from django.shortcuts import redirect
from .update_event import gupdate_event, get_single_event
# Create your views here.

def index(request):
    return render(request, 'index.html')

def elements(request):
    return render(request, 'elements.html')

def charts(request):
    return render(request, 'charts.html')

def panels(request):
    return render(request, 'panels.html')

def notifications(request):
    return render(request, 'notifications.html')

def page_profile(request):
    return render(request, 'page-profile.html')

def page_login(request):
    return render(request, 'page-login.html')

def page_lockscreen(request):
    return render(request, 'page-lockscreen.html')

def tables(request):
    return render(request, 'tables.html')

def typography(request):
    return render(request, 'typography.html')

def icons(request):
    return render(request, 'icons.html')


def calendar(request):
    if request.method == 'POST':
        form = add_event(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            event_date = form.cleaned_data['event_date']
            event_time = form.cleaned_data['event_time']
            dateTime = str(event_date)+"T"+str(event_time)+"+05:30"
            #Adding event to google calendar
            events = ginsert(title=title, dateTime=dateTime)
            return render(request, 'calendar.html', {'form':add_event(), 'events':events})
    else:
        events = get_event()
        form = add_event()
    return render(request, 'calendar.html', {'form':form, 'events':events})

def delete_event(request, event_id):
    form = add_event()
    gevent_delete(event_id=event_id)
    events = get_event()
    return render(request, 'calendar.html', {'form':form, 'events':events})

def update_event(request, event_id):
    event = get_single_event(event_id)
    form = add_event(event)
    events = get_event()
    form = add_event()
    return render(request, 'calendar.html', {'form':form, 'events':events})
