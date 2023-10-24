from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Classes(models.Model):
    classe_niveau=(("P","Primaire"),("C","Collège"),("L","Lycée"))
    id=models.AutoField(primary_key=True)
    niveau=models.CharField(default="C",choices=classe_niveau,max_length=10)
    classe_name=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

    def __str__(self):
        return f"{self.niveau} {self.classe_name}"

class CustomUser(AbstractUser):
    user_type_data=((1,"Admin"),(2,"Gérand"),(3,"Agent"), (4,"Eleve"), (5,"Enseignant"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=15)

class AdminUser(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()
    
class GerandUser(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()
    
class AgentUser(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()
    
class EleveUser(models.Model):
    id=models.AutoField(primary_key=True)
    sexe=(("F","Féminin"), ("M","Masculin"))
    genre=models.CharField(default=1,choices=sexe,max_length=15)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    classe=models.ForeignKey(Classes,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()
    
class EnseignantUser(models.Model):
    id=models.AutoField(primary_key=True)
    sexe=(("F","Féminin"), ("M","Masculin"))
    genre=models.CharField(default=1,choices=sexe,max_length=15)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()
    
