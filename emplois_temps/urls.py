from django.urls import path
from emplois_temps import views


urlpatterns = [
    path('programmeseance1', views.programme_seance, name='programmeseance1'),
    path('all_events/', views.all_events, name='all_events'),
    path('update_cour/', views.update_cour, name='update_cour'),
    
    
]