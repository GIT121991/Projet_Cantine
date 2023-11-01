from django.urls import path
from App_Cantine import views
app_name = 'app_cantine'

urlpatterns = [
    path('', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('classes/', views.classes, name='classes'),
    path('niveaux/', views.createNiveau, name='niveaux'),
    path('supprimer-classe>/', views.removeClasse, name='removeClasse'),
    path('abonnements/', views.abonnements, name='abonnements'),
    path('supprimer-abonnement/', views.removeAbonnement, name='removeAbonnement'),
    path('modifier-abonnement/<int:abonnement_id>/', views.editAbonnement, name='editAbonnement'),
    path('abonnement/', views.abonnement, name='abonnement'),
    path('abonner/<int:element_id>/', views.abonner, name='abonner'),
    path('abonnes/', views.abonnes, name='abonnes'),
    path('desabonner/<int:element_id>/', views.desabonner, name='desabonner'),
]
