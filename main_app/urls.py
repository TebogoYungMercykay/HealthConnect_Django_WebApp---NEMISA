from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('admin_ui', views.admin_ui, name='admin_ui'),
    path('patient_ui', views.patient_ui, name='patient_ui'),
    path('doctor_ui', views.doctor_ui, name='doctor_ui'),
    path('patient_profile/<int:patient_id>', views.patient_profile, name='patient_profile'),
    path('doctor_profile/<int:doctor_id>', views.doctor_profile, name='doctor_profile')
]
