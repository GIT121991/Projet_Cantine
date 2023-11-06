from django.urls import path
from App_Cantine import views


app_name = 'app_cantine'

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


]
