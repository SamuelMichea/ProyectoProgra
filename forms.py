from django import forms
from django.forms import ModelForm, fields
from .models import Obra

class ObraForm(ModelForm):

    class Meta:
        model = Obra
        fields = ['idObra','nombre','descripcion','precio']