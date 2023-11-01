from django import forms
from .models import TypeAbonnements

class TypeAbonnementsForm(forms.ModelForm):
    class Meta :
        model = TypeAbonnements
        fields = ['type', 'priceTeacher', 'priceStudent']
        labels = {'type': 'Type', 'priceTeacher': 'Prix enseignant', 'priceStudent': 'Prix élève'}