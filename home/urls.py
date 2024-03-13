from django.contrib import admin
from django.urls import path
from . import views
from .views import register, profile
urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]