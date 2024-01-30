from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # Temporary Routes for Testing Purpose Only
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('contact', views.contact, name="contact"),
    path('sendmail', views.sendmail, name="sendmail"),
    path('calendar', views.calendar , name='calendar'),
    # Ends Here
    path('help', views.help, name="help"),
    path('home_id/<str:fragment>/', views.home_id, name="home_id"),
]
