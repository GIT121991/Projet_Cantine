from django import forms
from .models import TypeAbonnements, CustomUser, Classes
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
        fields = ['type', 'priceTeacher', 'priceStudent', 'duree_jours']
        labels = {'type': 'Type', 'priceTeacher': 'Prix enseignant', 'priceStudent': 'Prix élève', 'duree_jours': 'Durée jours'}
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control'}),
            'priceTeacher': forms.NumberInput(attrs={'class': 'form-control'}),
            'priceStudent': forms.NumberInput(attrs={'class': 'form-control'}),
            'duree_jours': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class StudentForm(forms.ModelForm):
    classe = forms.ModelChoiceField(queryset = Classes.objects.all(), label='Classe', widget=forms.Select(attrs={'class': 'form-control', 'style': 'width:30%'}))
    type_abonnement = forms.ModelChoiceField(queryset = TypeAbonnements.objects.all(), label='Type d\'bonnement', widget=forms.Select(attrs={'class': 'form-control', 'style': 'width:30%'}))
    class Meta :
        model = CustomUser
        fields = ['lastname', 'firstname', 'genre', 'user_type', 'classe', 'is_abonne', 'type_abonnement']
        labels = {'lastname':'NOM', 'firstname':'Prénoms', 'genre':'Sexe', 'user_type': 'Type d\'utilisateur', 'is_abonne': 'est abonné?'}
        widgets = {
            'lastname': forms.CharField().widget.attrs.update({'class': 'form-control'}),
            'firstname': forms.CharField().widget.attrs.update({'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-control', 'style': 'width:30%'}),
            'user_type': forms.Select(attrs={'class': 'form-control', 'style': 'width:30%'}),
        }

class CustomUserForm(forms.ModelForm):
    class Meta :
        try:
            classe_list = [(classe.id, classe.classe_name) for classe in Classes.objects.all()]
        except:
            classe_list = []
        model = CustomUser
        fields = ['lastname', 'firstname', 'genre', 'user_type', 'classe']
        labels = {'lastname':'NOM', 'firstname':'Prénoms', 'genre':'Sexe', "user_type": "Type d'utilisateur", 'classe':'Classes'}
        widgets = {
            'lastname': forms.TextInput(attrs={"class": "form-control", "autocomplete": "off"}),
            'firstname': forms.TextInput(attrs={"class": "form-control", "autocomplete": "off"}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
            'user_type': forms.Select(attrs={'class': 'form-control'}),
            'classe': forms.Select(attrs={"class": "form-control"}, choices=classe_list),

        }

