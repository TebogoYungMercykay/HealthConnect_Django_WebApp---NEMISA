from django.urls import path
from . import views

urlpatterns = [
    path('consultation', views.consultation , name='consultation'),
    path('make_consultation', views.make_consultation , name='make_consultation'),
    path('consultation_view/<int:consultation_id>', views.consultation_view , name='consultation_view'),
    path('close_consultation/<int:consultation_id>', views.close_consultation , name='close_consultation'),
    path('create_review/<int:doctor_id>', views.create_review , name='create_review'),
    path('get_reviews_id/<int:doctor_id>', views.get_reviews_id , name='get_reviews_id'),
    path('get_reviews', views.get_reviews , name='get_reviews')
]  
