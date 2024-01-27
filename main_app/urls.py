from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # Temporary Routes for Testing Purpose Only
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('contact', views.contact, name="contact"),
    path('sendmail', views.sendmail, name="sendmail"),
    path('consultation', views.consultation, name="consultation"),
    path('consultation_chats', views.consultation_chats, name="consultation_chats"),
    path('admin_page', views.admin_page, name="admin_page"),
    path('calendar', views.calendar , name='calendar'),
    # Ends Here
    path('help', views.help, name="help"),
    path('home_id/<str:fragment>/', views.home_id, name="home_id"),
    
    path('login_temp', views.login_temp, name="login_temp"),
]
