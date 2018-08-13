from django.urls import path, include

from accounts import views

urlpatterns = [
        path('', views.dashboard, name='dashboard'),
        path('',include('django.contrib.auth.urls')),
        ]

