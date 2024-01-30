"""HealthconnectBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("main_app.urls")),
    path('admin/', admin.site.urls),
    path('adminpages/', include("healthconnect_backend.admin.urls")),
    path("users/", include("healthconnect_backend.accounts.urls")),
    path("auth/", include("healthconnect_backend.auth.urls")),
    path("consultations/", include("healthconnect_backend.consultations.urls")),
    path("chats/", include("healthconnect_backend.chats_and_feedback.urls")),
    path("disease_prediction/", include("healthconnect_backend.disease_prediction.urls")),
    path("posts/", include("healthconnect_backend.posts.urls"))
]
