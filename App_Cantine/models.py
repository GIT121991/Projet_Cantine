from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Niveau(models.Model):
    classe_niveau = [("P", "Primaire"), ("C", "Collège"), ("L", "Lycée")]
    id = models.AutoField(primary_key=True)
    name = models.CharField(default="C", choices=classe_niveau, max_length=15)

    def __str__(self):
        return f"{self.name}"

class Classes(models.Model):
    id=models.AutoField(primary_key=True)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    classe_name=models.CharField(unique=True, max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

    def __str__(self):
        return f"{self.classe_name}"


class TypeAbonnements(models.Model):
    types = [("Aucun", "Aucun"), ("3 jours", "3 jours"), ("Hebdomadaire", "Hebdomadaire"), ("Mensuel", "Mensuel"), ("Trimestriel", "Trimestriel")]
    id = models.AutoField(primary_key=True)
    type = models.CharField(default="3 jours", choices=types, max_length=20, unique = True)
    priceTeacher = models.IntegerField(default = 1000)
    priceStudent = models.IntegerField(default = 1000)
    duree_jours = models.IntegerField()
    def __str__(self):
        return self.type

class CustomUser(models.Model):
    lastname=models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    sexe = [("F", "Féminin"), ("M", "Masculin")]
    genre = models.CharField(default="M", choices=sexe, max_length=1)
    user_type_data = [("Admin", "Admin"), ("Gérand", "Gérand"), ("Agent", "Agent"), ("Eleve", "Eleve"), ("Enseignant", "Enseignant")]
    user_type = models.CharField(default="Eleve", choices=user_type_data, max_length=50)
    classe = models.ForeignKey(Classes, on_delete=models.CASCADE, blank=True, null=True)
    is_abonne = models.BooleanField(default=False)
    type_abonnement = models.ForeignKey(TypeAbonnements, on_delete=models.CASCADE, blank=True, null=True)
    date_abonnement = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.lastname} {self.firstname}"
