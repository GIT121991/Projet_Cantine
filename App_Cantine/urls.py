from django.urls import path
from App_Cantine import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_page, name='login_page'),
    path('logout', views.logout_page, name='logout_page'),
    path('register', views.register_page, name='register_page'),
    path('manager', views.manager, name='user_manager'),
    path('update-manager', views.updateManager, name='updateManager'),
    path('get_manager_info/<int:manager_id>/', views.get_manager_info, name='get_manager_info'),
    path('supprimer-manager', views.removeManager, name='removeManager'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('classes', views.classes, name='classes'),
    path('niveaux', views.createNiveau, name='niveaux'),
    path('supprimer-classe', views.removeClasse, name='removeClasse'),
    # path('', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('classes/', views.classes, name='classes'),
    path('niveaux/', views.createNiveau, name='niveaux'),
    path('supprimer-classe/', views.removeClasse, name='removeClasse'),
    path('typeAbonnements/', views.typeAbonnements, name='typeAbonnements'),
    path('supprimer-abonnement/', views.removeAbonnement, name='removeAbonnement'),
    path('modifier-abonnement/<int:abonnement_id>/', views.editAbonnement, name='editAbonnement'),
    path('abonnement/', views.abonnement, name='abonnement'),
    path('abonner/<int:element_id>/', views.abonner, name='abonner'),
    path('abonnes/', views.abonnes, name='abonnes'),
    path('desabonner/<int:element_id>/', views.desabonner, name='desabonner'),

]
