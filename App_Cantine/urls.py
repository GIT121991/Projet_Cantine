from django.urls import path

from App_Cantine import views

urlpatterns = [
    path('', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('classes', views.classes, name='classes'),
]
