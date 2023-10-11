from django.urls import path

from App_Cantine import views

urlpatterns = [
    path('', views.index, name='index'),
    
]
