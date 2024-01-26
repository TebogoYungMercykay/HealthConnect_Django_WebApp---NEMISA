from django.urls import path
from . import views

urlpatterns = [
    path('post_feedback/<int:user_id>', views.post_feedback, name='post_feedback'),
    path('user_feedback/<int:user_id>', views.user_feedback, name='user_feedback'),
    path('chat_messages/<int:user_id>', views.chat_messages, name='chat_messages'),
    path('create_chat/<int:user_id>', views.create_chat, name='create_chat'),
    path('whatsapp', views.whatsapp, name='whatsapp'),
    path('meeting',views.meeting, name='meeting'),

]
