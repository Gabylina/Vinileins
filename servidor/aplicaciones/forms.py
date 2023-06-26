from django import forms
from .models import Cliente, Pedido, Vinilo,Administrador

class formCrearVinilo(forms.ModelForm):
    
    class Meta:
        model=Vinilo
        fields=["cara_delante","cara_detras", "nombre_cantante", "nombre_vinilo", "estilo","precio"]

class formCrearAdmin(forms.ModelForm):
    
    class Meta:
        model=Administrador
        fields='__all__'

class formpedido(forms.ModelForm):
    
    class Meta:
        model=Pedido
        fields=["estado"]

class formCrearCliente(forms.ModelForm):
    
    class Meta:
        model=Cliente
        fields='__all__'