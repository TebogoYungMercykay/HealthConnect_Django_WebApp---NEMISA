# app_name/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('create_disease', views.create_disease , name='create_disease'),
    path('<int:user_id>', views.get_disease , name='get_disease'),
    path('check_disease/<int:disease_id>', views.check_disease , name='check_disease')
]
