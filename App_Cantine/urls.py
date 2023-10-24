from django.urls import path
from App_Cantine import views
app_name = 'app_cantine'

urlpatterns = [
    path('', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('classes', views.classes, name='classes'),
    path('supprimer-classe/<int:classe_id>/', views.removeClasse, name='removeClasse'),
]
