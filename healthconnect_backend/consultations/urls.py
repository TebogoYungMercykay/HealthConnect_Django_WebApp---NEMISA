from django.urls import path
from . import views

urlpatterns = [
    path('all_consultations/<int: id>', views.all_consultations , name='all_consultations'),
    path('make_consultation', views.make_consultation , name='make_consultation'),
    path('consultation_view_patient/<int:consultation_id>', views.consultation_view_patient , name='consultation_view_patient'),
    path('consultation_view_doctor/<int:consultation_id>', views.consultation_view_doctor , name='consultation_view_doctor'),
    path('consultation_history_patient', views.consultation_history_patient , name='consultation_history_patient'),
    path('consultation_history_doctor', views.consultation_history_doctor , name='consultation_history_doctor'),
    path('close_consultation/<int:consultation_id>', views.close_consultation , name='close_consultation'),
    path('create_review/<int:doctor_id>', views.create_review , name='create_review'),
    path('get_reviews_id/<int:doctor_id>', views.get_reviews_id , name='get_reviews_id'),
    path('get_reviews', views.get_reviews , name='get_reviews')
]  
