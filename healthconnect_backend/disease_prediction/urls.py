# app_name/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>', views.get_disease , name='get_disease'),
    path('check_disease/<int:user_id>/<int:disease_id>', views.check_disease , name='check_disease'),
    path('create_disease/<int:user_id>', views.create_disease , name='create_disease')
]
