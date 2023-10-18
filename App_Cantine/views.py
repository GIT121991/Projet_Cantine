from django.http import HttpResponse
from django.shortcuts import render

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