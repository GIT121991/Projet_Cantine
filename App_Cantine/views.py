from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Classes, Niveau
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