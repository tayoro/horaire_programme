from django import forms
from .models import Seance_cour, Seance_TD

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
    


class Seance_courForm(forms.ModelForm):
    #permet de mettre un calendrier dans le formulaire
    date_debut = forms.DateTimeField(
       # input_formats=["%m/%d/%Y, %H:%M:%S"],
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
            },
           # format="%m/%d/%Y, %H:%M:%S"
        )
    )
    date_fin = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
            }
        )
    )
    class Meta: # cree et configue notre formulaire , et se base sur le modèle employee 
        model = Seance_cour
        fields = ['id_seance_cour',
                  'filiere',
                  'salle',
                  'enseignant',
                  'date_debut',
                  'date_fin',
                  'niveau',
                  'cour',             
        ]
        labels = {'date_debut': ' ', 'date_fin': ' '}
        
    def clean(self):
        cleaned_data = super().clean()
        date_debut = cleaned_data.get("date_debut")
        date_fin = cleaned_data.get("date_fin")
        if date_fin < date_debut :
            raise forms.ValidationError("La date de fin doit etre plus grand que la date debut")
        
        
        
        
class Seance_TdForm(forms.ModelForm):
    date_debut = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
            }
        )
    )
    date_fin = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
            }
        )
    )
    class Meta: # cree et configue notre formulaire , et se base sur le modèle employee 
        model = Seance_TD
        fields = ['id_seance_td',
                  'filiere',
                  'salle',
                  'enseignant',
                  'date_debut',
                  'date_fin',
                  'niveau',
                  'cour',
                  'group_td', 
                        
        ]
        labels = {'date_debut': '', 'date_fin': ''}
        
    def clean(self):
        cleaned_data = super().clean()
        date_debut = cleaned_data.get("date_debut")
        date_fin = cleaned_data.get("date_fin")
        if date_fin < date_debut :
            raise forms.ValidationError("La date de fin doit etre superieur que la date debut")
    