from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard , name='dashboard'),
    path('diseaseinfos', views.diseaseinfos , name='diseaseinfos'),
    path('sendmail', views.sendmail , name='sendmail'),
]  
