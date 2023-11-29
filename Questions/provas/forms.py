from django import forms
from .models import Prova

class ProvaSelectForm(forms.Form):
    prova = forms.ModelChoiceField(queryset=Prova.objects.all(), empty_label=None)
