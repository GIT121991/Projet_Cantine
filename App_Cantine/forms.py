from django import forms

class ClassForm(forms.Form):
    niveaux = [("P","Primaire"),("C","Collège"),("L","Lycée")]
    niveau  = forms.choiceField(choices= niveaux)

    classes = ['Maternelle','CI','CP','CE1','CE2','CM1','CM2','6eme','5eme','4eme','3eme','2nd','1ere','Tle']
    classe = forms.choiceField(choices= classes)