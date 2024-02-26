from django import forms
from .forms import VoitureForm



class VoitureForm(forms.ModelForm):
	class Meta:
		model = Voiture
		fields = ['marque','annee_fabrication']