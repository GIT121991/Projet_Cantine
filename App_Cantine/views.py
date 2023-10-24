from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Classes

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
        section = request.POST.get("section")
        classe = request.POST.get("classe")
        room = Classes.objects.create(niveau=section, classe_name=classe)
        room.save()
        return redirect("classes")
    else:
        room = Classes.objects.all()
        return render(request,'classes.html', {'classes':room})
