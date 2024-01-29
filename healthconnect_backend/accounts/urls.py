from django.urls import path
from . import views

urlpatterns = [
    path('signup_patient', views.signup_patient, name="signup_patient"),
    path('signup_doctor', views.signup_doctor , name="signup_doctor"),
    path('savedata/<int:user_id>', views.savedata , name='savedata'),
    path('get_user', views.get_user , name='get_user'),
]