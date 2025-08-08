from django import forms
from .models import GroupeProjet

class GroupeProjetForm(forms.ModelForm):
    class Meta:
        model = GroupeProjet
        fields = ['nom', 'description']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'nom': 'Nom du Groupe de Projet',
            'description': 'Description',
        }
        help_texts = {
            'nom': 'Entrez le nom du groupe de projet.',
            'description': 'Entrez une description pour le groupe de projet.',
        }