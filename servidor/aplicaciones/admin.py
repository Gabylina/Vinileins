from django.contrib import admin
from django.utils.html import format_html
from .models import Cliente, Administrador, Vinilo, Carrito

###################ESTO ES DE INGENERIA EN INFORMATICA############################

from .models import Presupuesto
# Register your models here.

class admCliente(admin.ModelAdmin):
    list_display=["rut","nombre","apellido","correo","contra","direccion","region","comuna","telefono"]
    
    class meta:
        model=Cliente

class admAdministrador(admin.ModelAdmin):
    list_display=["rut","nombre","correo","contra","telefono","cargo"]
    list_editable=["nombre","correo","contra","telefono","cargo"]
    
    class meta:
        model=Administrador

class admVinilo(admin.ModelAdmin):
    list_display=["id","cara_delante","cara_detras","nombre_cantante","nombre_vinilo","estilo","precio","cara_delante_foto","cara_detras_foto"]
    list_editable=["cara_delante","cara_detras","nombre_cantante","nombre_vinilo","estilo","precio"]

    class meta:
        model=Vinilo

    def cara_delante_foto(self, obj):
        return format_html('<img src={} height="100px" width="100px" />', obj.cara_delante.url)
    def cara_detras_foto(self, obj):
        return format_html('<img src={} height="100px" width="100px" />', obj.cara_detras.url)

class admCarrito(admin.ModelAdmin):
    list_display=["id","user","producto","cantidad"]

    class meta:
        model=Carrito

admin.site.register(Cliente,admCliente)
admin.site.register(Administrador,admAdministrador)
admin.site.register(Vinilo,admVinilo)
admin.site.register(Carrito,admCarrito)



###################ESTO ES DE INGENERIA EN INFORMATICA############################
class admPresupuesto(admin.ModelAdmin):
    list_display=["id","cliente","descripcion","monto"]
    
    class meta:
        model=Presupuesto

admin.site.register(Presupuesto,admPresupuesto)