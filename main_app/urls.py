from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('consultations',views.consultation_home,name='consulation_home'),
    path('consultations/self_diagnose',views.self_diagnose,name='self_diagnose'),
    # Temporary Routes for Testing Purpose Only
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('contact', views.contact, name="contact"),
    path('sendmail', views.sendmail, name="sendmail"),
    path('admin_page', views.admin_page, name="admin_page"),
    path('calendar', views.calendar , name='calendar'),
    path('page', views.page , name='page'),
    path('terms_and_conditions', views.terms_and_conditions , name='get_terms_and_conditions'),
    # Ends Here
    path('help', views.help, name="help"),
    path('home_id/<str:fragment>/', views.home_id, name="home_id"),
    
    path('login_temp', views.login_temp, name="login_temp"),
]
