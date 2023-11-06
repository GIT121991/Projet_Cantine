from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Classes, Niveau, TypeAbonnements, CustomUser
from .forms import TypeAbonnementsForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate, logout
from .forms import CustomLoginForm, LoginForm, RegisterForm
from django.contrib.auth.hashers import make_password


# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = CustomLoginForm

    def form_valid(self, form):
        # Connexion de l'utilisateur
        user = form.get_user()
        print(user)
        login(user)

        # Vérifie si l'utilisateur est le superutilisateur et a choisi de créer un autre utilisateur
        if user.is_superuser and form.cleaned_data.get('create_user'):
            # Redirection vers la création d'utilisateur
            return redirect('dashboard')  # Remplacez 'creer_utilisateur' par l'URL de création d'utilisateur
        else:
            # Redirection vers l'application
            return redirect('dashboard')  # Remplacez 'votre_application' par l'URL de l'application

def login_page(request):
    if request.method == 'POST':
        username =request.POST.get("username")
        password = request.POST.get("password")
        create_user = request.POST.get("newuser")
        print(create_user)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            message = f'Bonjour, {user.username}! Vous êtes connecté.'
            if create_user is not None and user.is_superuser:
                return redirect('app_cantine:register_page')
            return redirect('app_cantine:dashboard')
        else:
            message = 'Identifiants invalides.'
            return render(request, 'login.html')


def logout_page(request):
    logout(request)
    messages.success(request, "Vous êtes déconnecter")
    return redirect('app_cantine:index')

def register_page(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        last_name = request.POST.get("last_name")
        first_name = request.POST.get("first_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        is_superuser = request.POST.get("is_superuser")
        if is_superuser is None:
            is_superuser=0
        new_user = User.objects.create_user(username=username,
                                            last_name=last_name,
                                            first_name=first_name,
                                            email=email,
                                            password=password,
                                            is_superuser=is_superuser)
        new_user.save()
        return redirect("app_cantine:index")

    else:
        messages.error(request, 'Formulaire invalide')
        return render(request, 'register.html')

def manager(request):

    managers=User.objects.all()
    return render(request, 'liste_user.html', {'managers':managers})

def get_manager_info(request, manager_id):
    utilisateur = User.objects.get(id=manager_id)
    try:
        user_info = {
            'username': utilisateur.username,
            'last_name': utilisateur.last_name,
            'first_name': utilisateur.first_name,
            'email': utilisateur.email,
            }
        return JsonResponse(user_info)
    except User.DoesNotExist:
        return JsonResponse({'error': 'Utilisateur non trouvé'}, status=404)
def updateManager(request):
    if request.POST.get('managerId'):
        username = request.POST.get("username")
        last_name = request.POST.get("last_name")
        first_name = request.POST.get("first_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        is_superuser = request.POST.get("is_superuser")
        if is_superuser is None:
            is_superuser = 0
        try:
            manager_id = request.POST.get('managerId')
            print(manager_id)
            utilisateur = User.objects.get(pk=manager_id)
            utilisateur.username = username
            utilisateur.last_name = last_name
            utilisateur.first_name = first_name
            utilisateur.email = email
            utilisateur.is_superuser = is_superuser
            if password:
                password = make_password(password)
                utilisateur.password = password
            utilisateur.save()
            messages.success(request, f"Modification effectuée avec succès")
        except Exception as e:
            messages.error(request, f"Modification non effectuée. {e}")
        return redirect("app_cantine:user_manager")

def removeManager(request):
    if request.POST.get('manager_id'):
        try:
            manager = User.objects.get(pk=request.POST.get('manager_id'))
            manager.delete()
            messages.success(request, f"L'utilisateur {manager.username} a été supprimer avec succès")
        except Exception as e:
            messages.error(request, f"Desoler nous avons rencontré une erreur {e}.")
    return redirect("app_cantine:user_manager")

def index(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request,'Dashboard.html')

def classes(request):
    if request.method == "POST":
        niveau_id = request.POST.get("niveau_id")
        classe = request.POST.get("classe")
        try:
            room = Classes.objects.create(classe_name=classe, niveau_id=niveau_id)
            room.save()
            messages.success(request, f"La classe de {classe} a été crée avec succès")
        except:
            messages.error(request, "Cette classe existe déjà.")
        return redirect("app_cantine:classes")

    else:
        niveaux = Niveau.objects.all()
        room = Classes.objects.all()
        return render(request,'classes.html', {'classes':room, 'niveaux':niveaux})

    
def removeClasse(request):
    if request.POST.get('classe_id'):
        try:
            classe = Classes.objects.get(pk=request.POST.get('classe_id'))
            classe.delete()
            messages.success(request, f"La classe de {classe.classe_name} a été supprimer avec succès")
        except Exception as e:
            messages.error(request, f"Desoler nous avons rencontré une erreur {e}.")
    return redirect("app_cantine:classes")
def createNiveau(request):
    if request.method == "POST":
        section = request.POST.get("section")
        niveau = Niveau.objects.create(name=section)
        niveau.save()
    return redirect("app_cantine:classes")

def abonnements(req):
    if req.method == "POST":
        form = TypeAbonnementsForm(req.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(req, "Ajout de type d'abonnement avec succès")
            except:
                messages.error(req, "Cet abonnement existe déjà")
            return redirect("app_cantine:abonnements")
    else:
        form = TypeAbonnementsForm()
        return render(req, 'type-abonnements.html', { 'form': form , 'abonnements': TypeAbonnements.objects.all()} )
    

def removeAbonnement(req):
    if req.POST.get('abonnement_id'):
        try:
            abonnement = TypeAbonnements.objects.get(pk=req.POST.get('abonnement_id'))
            abonnement.delete()
            messages.success(req, f"L'abonnement {abonnement.type} a été supprimé avec succès")
        except Exception as e:
            messages.error(req, f"Désoler nous avons rencontré une erreur {e}.")
    return redirect("app_cantine:abonnements")


def editAbonnement(req, abonnement_id):
    abonnement = TypeAbonnements.objects.get(pk = abonnement_id)
    abonne = abonnement
    abonnement.delete()
    if req.method == 'POST':
        form = TypeAbonnementsForm(req.POST, instance=abonne)
        if form.is_valid():
            form.save()
            return redirect("app_cantine:abonnements")
    else:
        form = TypeAbonnementsForm(instance=abonne)
    return render(req, 'type-abonnements.html', { 'form': form , 'abonnements': TypeAbonnements.objects.all()} )


def abonnement(req):
    teachersAndStudents = CustomUser.objects.all().filter(is_abonne = False)
    typeAbonnements = TypeAbonnements.objects.all()
    return render(req, 'abonnement.html', {"typeAbonnements": typeAbonnements, "teachers": teachersAndStudents.filter(user_type = 5), "students": teachersAndStudents.filter(user_type = 4)})


def abonner(req, element_id):
    element = CustomUser.objects.get(pk = element_id)
    if req.method == 'POST':
        typeAbonnementId = req.POST.get("type_abonnement_id")
        element.is_abonne = True
        element.type_abonnement_id = typeAbonnementId
        element.save()
    return redirect("app_cantine:abonnement")


def abonnes(req):
    teachersAndStudents = CustomUser.objects.all().filter(is_abonne = True)
    return render(req, 'abonnes.html', {"teachers": teachersAndStudents.filter(user_type = 5), "students": teachersAndStudents.filter(user_type = 4)})


def desabonner(req, element_id):
    element = CustomUser.objects.get(pk = element_id)
    element.is_abonne = False
    element.save()
    return redirect("app_cantine:abonnes")