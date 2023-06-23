from django import forms
from .models import Vinilo

class formCrearVinilo(forms.ModelForm):
    
    class Meta:
        model=Vinilo
        fields=["cara_delante","cara_detras", "nombre_cantante", "nombre_vinilo", "estilo","precio"]

class formModificarVinilo(forms.ModelForm):
    
    class Meta:
        model=Vinilo
        fields='__all__'
        #["cara_delante","cara_detras", "nombre_cantante", "nombre_vinilo", "estilo","precio"]
