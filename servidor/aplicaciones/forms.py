from django import forms
from .models import Vinilo,Administrador

class formCrearVinilo(forms.ModelForm):
    
    class Meta:
        model=Vinilo
        fields=["cara_delante","cara_detras", "nombre_cantante", "nombre_vinilo", "estilo","precio"]

class formCrearAdmin(forms.ModelForm):
    
    class Meta:
        model=Administrador
        fields='__all__'
       