from django.urls import path
from . import views

urlpatterns = [
    path('consultation', views.consultation , name='consultation'),
    path('find_doctor',views.get_doctors,name='find_doctor'),
    path('make_consultation', views.make_consultation , name='make_consultation'),
    path('consultation_view/<int:consultation_id>', views.consultation_view , name='consultation_view'),
    path('close_consultation/<int:consultation_id>', views.close_consultation , name='close_consultation'),
    path('create_review/<int:doctor_id>', views.create_review , name='create_review'),
    path('rate_prediction/<int:consultation_id>', views.rate_prediction , name='rate_prediction'),
    path('get_reviews_id/<int:doctor_id>', views.get_reviews_id , name='get_reviews_id'),
    path('get_reviews', views.get_reviews , name='get_reviews'),
    path('videoconsultation/<int:consultation_id>',views.lauchvideocaller,name='consultation_call'),
    path('videoconsultation_live/<int:consultation_id>',views.getToken,name='open_video_consultation')
]  

# {
#     "doctor_id": 10,
#     "diseaseinfo_id": 43,
#     "consultation_id": 17,
#     "rating": 4,
#     "symptoms": ["Fever", "Headache", "Fatigue"],
#     "diseasename": "Common Cold"
# }