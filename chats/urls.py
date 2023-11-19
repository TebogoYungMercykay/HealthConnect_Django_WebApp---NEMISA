from django.urls import path , include
from . import views

urlpatterns = [
  path('post_feedback', views.post_feedback, name='post_feedback'),
  path('get_feedback', views.get_feedback, name='get_feedback'),
  path('whatsapp', views.whatsapp, name='whatsapp'),
  path('meeting',views.videocall, name='meeting'),
]
