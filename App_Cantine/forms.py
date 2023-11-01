from django import forms
from .models import TypeAbonnes

class TypeAbonnesForm(forms.ModelForm):
    class Meta :
        model = TypeAbonnes
        fields = ['type', 'priceTeacher', 'priceStudent']
        labels = {'type': 'Type', 'priceTeacher': 'Prix enseignant', 'priceStudent': 'Prix élève'}