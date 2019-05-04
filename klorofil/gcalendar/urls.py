from django.urls import path
from . import views

app_name = "gcalendar"

urlpatterns = [
    path('', views.index, name="dashboard"),
    path('elements/', views.elements, name="elements"),
    path('charts/', views.charts, name="charts"),
    path('panels/', views.panels, name="panels"),
    path('notifications/', views.notifications, name="notifications"),
    path('page-profile/', views.page_profile, name="page_profile"),
    path('page_login/', views.page_login, name="page_login"),
    path('page_lockscreen/', views.page_lockscreen, name="page_lockscreen"),
    path('tables/', views.tables, name="tables"),
    path('typography/', views.typography, name="typography"),
    path('icons/', views.icons, name="icons"),
    path('calendar/', views.calendar, name='calendar'),
    path('delete/<str:event_id>', views.delete_event, name="delete_event"),
    path('update/<str:event_id>', views.update_event, name="update_event"),
]
