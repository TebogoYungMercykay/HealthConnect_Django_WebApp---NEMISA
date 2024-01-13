from django.urls import path
from . import views

urlpatterns = [
    path('login/patient', views.login_patient , name='login_patient'),
    path('login/doctor', views.login_doctor , name='login_doctor'),
    path('login/admin', views.login_admin , name='login_admin'),
    path('logout', views.logout , name='logout'),
]
