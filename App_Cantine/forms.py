from django import forms
from .models import TypeAbonnements, CustomUser, Classes, Student
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomLoginForm(AuthenticationForm):
    create_user = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

class RegisterForm(UserCreationForm):
    model = get_user_model()
    username = forms.CharField(max_length=63, label='Nom d’utilisateur',
                               widget=forms.TextInput(attrs={"class": "form-control", "autocomplete": "off"}))
    lastname = forms.CharField(max_length=63, label='Nom de famille',
                               widget=forms.TextInput(attrs={"class": "form-control", "autocomplete": "off"}))
    firstname = forms.CharField(max_length=63, label='Prénoms',
                               widget=forms.TextInput(attrs={"class": "form-control", "autocomplete": "off"}))
    email = forms.EmailField(max_length=63, label='Adresse mail',
                               widget=forms.EmailInput(attrs={"class": "form-control", "autocomplete": "off"}))
    password1 = forms.CharField(max_length=63, label='Mot de passe',
                               widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(max_length=63, label='Confirme mot de passe',
                               widget=forms.PasswordInput(attrs={"class": "form-control"}))
    super_user = forms.BooleanField(label='Super utilisateur',
        required=False,
        initial=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Nom d’utilisateur',
                               widget=forms.TextInput(attrs={"class":"form-control","autocomplete":"off"}))
    password = forms.CharField(max_length=63,label='Mot de passe',
                               widget=forms.PasswordInput(attrs={"class":"form-control"}))
    create_user = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

class TypeAbonnementsForm(forms.ModelForm):
    class Meta :
        model = TypeAbonnements
        fields = ['type', 'daysNumber', 'priceTeacher', 'priceStudent']
        labels = {'type': 'Type', 'daysNumber': 'Nombre de jours', 'priceTeacher': 'Prix enseignant', 'priceStudent': 'Prix élève'}
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control'}),
            'daysNumber': forms.Select(attrs={'class': 'form-control'}),
            'priceTeacher': forms.NumberInput(attrs={'class': 'form-control'}),
            'priceStudent': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class StudentForm(forms.ModelForm):
    classe = forms.ModelChoiceField(queryset = Classes.objects.all())
    type_abonnement = forms.ModelChoiceField(queryset = TypeAbonnements.objects.all())
    class Meta :
        model = CustomUser
        fields = ['lastname', 'firstname', 'genre', 'user_type', 'classe', 'is_abonne', 'type_abonnement']
        labels = {'lastname':'NOM', 'firstname':'Prénoms', 'genre':'Sexe'}
        widgets = {
            'lastname': forms.CharField().widget.attrs.update({'class': 'form-control'}),
            'firstname': forms.CharField().widget.attrs.update({'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
            'user_type': forms.Select()
        }

class TeacherForm(forms.ModelForm):
    type_abonnement = forms.ModelChoiceField(queryset = TypeAbonnements.objects.all())
    class Meta :
        model = CustomUser
        fields = ['lastname', 'firstname', 'genre', 'user_type', 'is_abonne', 'type_abonnement']
        labels = {'lastname':'NOM', 'firstname':'Prénoms', 'genre':'Sexe'}
        widgets = {
            'lastname': forms.CharField().widget.attrs.update({'class': 'form-control'}),
            'firstname': forms.CharField().widget.attrs.update({'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
            'user_type': forms.Select()
        }

