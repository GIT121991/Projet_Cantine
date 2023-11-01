from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Classes, Niveau, TypeAbonnes, CustomUser
from .forms import TypeAbonnesForm
from django.contrib import messages

# Create your views here.
def index(request):
    prenom = "Issa"
    nom = "GOUNOU"
    nombre = range(1,100)
    print(nombre)
    return render(request, 'index.html', {"prenom2":prenom, "nom2":nom, "nbre":nombre})

def dashboard(request):
    return render(request,'Dashboard.html')

def login(request):
    return render(request,'login.html')

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
        form = TypeAbonnesForm(req.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(req, "Ajout de type d'abonnement avec succès")
            except:
                messages.error(req, "Cet abonnement existe déjà")
            return redirect("app_cantine:abonnements")
    else:
        form = TypeAbonnesForm()
        return render(req, 'abonnements.html', { 'form': form , 'abonnements': TypeAbonnes.objects.all()} )
    

def removeAbonnement(req):
    if req.POST.get('abonnement_id'):
        try:
            abonnement = TypeAbonnes.objects.get(pk=req.POST.get('abonnement_id'))
            abonnement.delete()
            messages.success(req, f"L'abonnement {abonnement.type} a été supprimé avec succès")
        except Exception as e:
            messages.error(req, f"Désoler nous avons rencontré une erreur {e}.")
    return redirect("app_cantine:abonnements")


def editAbonnement(req, abonnement_id):
    abonnement = TypeAbonnes.objects.get(pk = abonnement_id)
    abonne = abonnement
    abonnement.delete()
    if req.method == 'POST':
        form = TypeAbonnesForm(req.POST, instance=abonne)
        if form.is_valid():
            form.save()
            return redirect("app_cantine:abonnements")
    else:
        form = TypeAbonnesForm(instance=abonne)
    return render(req, 'abonnements.html', { 'form': form , 'abonnements': TypeAbonnes.objects.all()} )


def abonnement(req):
    teachersAndStudents = CustomUser.objects.all().filter(is_abonne = False)
    return render(req, 'abonnement.html', {"teachers": teachersAndStudents.filter(user_type = 5), "students": teachersAndStudents.filter(user_type = 4)})


def abonnes(req):
    
    return render(req, 'abonnes.html', {"abonnes": CustomUser.objects.all().filter(is_abonne = True)})