from django import forms
from .models import Cliente, Vinilo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class formCrearVinilo(forms.ModelForm):
    
    class Meta:
        model=Vinilo
        fields=["cara_delante","cara_detras", "nombre_cantante", "nombre_vinilo", "estilo","precio"]

class formModificarVinilo(forms.ModelForm):
    
    class Meta:
        model=Vinilo
        fields='__all__'
        #["cara_delante","cara_detras", "nombre_cantante", "nombre_vinilo", "estilo","precio"]

class formCrearCli(UserCreationForm):
    
    class Meta:
        model =User
        fields=["username","first_name","last_name","email","password1",'password2']
        

