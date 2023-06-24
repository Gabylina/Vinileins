from django.shortcuts import render,get_object_or_404,redirect
from datetime import date
from .models import Administrador, Cliente,Vinilo
from .forms import formCrearVinilo,formCrearAdmin
from django.db.models import Q
# Create your views here.

def index(request):
    admin=Administrador.objects.all()
    
    print("a")
    contexto={
        "admins":admin,
    }
    
    return render(request,'aplicaciones/index.html',contexto)

def otrawea(request):
    v=Vinilo.objects.all()

    contexto={
        "v":v,
    }

    return render(request,'aplicaciones/otrawea.html',contexto)

def vinilos(request):
    vini=Vinilo.objects.all()
    
    contexto={
        "vini":vini,
    }
    
    return render(request,'aplicaciones/vinilos.html',contexto)

def añadir(request):
    form=formCrearVinilo(request.POST,request.FILES or None)
    
    contexto={
        "form":form,
    }
    
    if request.method=="POST":

        if form.is_valid():
            form.save()
            return redirect(to="vinilos")
    
    return render(request,'aplicaciones/añadirvinilo.html',contexto)

def modificarvinilo(request,id):
    Producto=get_object_or_404(Vinilo,id=id)
    
    contexto={
        'form':formCrearVinilo(instance=Producto)
    }
    
    if request.method=="POST":
                                    #and request.FILES
        formulario=formCrearVinilo(data=request.POST,files=request.FILES ,instance=Producto)

        if formulario.is_valid():
            formulario.save()
            return redirect(to="vinilos")
        contexto["form"]= formulario
        
    return render(request,'aplicaciones/modificarvinilo.html',contexto)

def eliminarvinilo(request,id):
    producto=get_object_or_404(Vinilo,id=id)

    contexto={

        "vin":producto
    }

    if request.method=="POST":
        producto.delete()
        return redirect(to="vinilos")


    return render(request,"aplicaciones/eliminarvinilo.html",contexto)

def añadiradmin(request):
    form=formCrearAdmin(request.POST or None)
    
    contexto={
        "form":form,
    }
    
    if request.method=="POST":

        if form.is_valid():
            form.save()
            return redirect(to="index")
    
    return render(request,'aplicaciones/añadiradmin.html',contexto)

def viniloscli(request):
    v=Vinilo.objects.all()

    contexto={
        "v":v,
    }

    return render(request,'aplicaciones/viniloscli.html', contexto)

def iniciocliente(request):
    v=Vinilo.objects.all()

    contexto={
        "v":v,
    }

    return render(request,'aplicaciones/iniciocliente.html',contexto)

def detalle(request, id):
    v=get_object_or_404(Vinilo,id=id)
    
    contexto={
        "v":v,
    }
    return render(request, 'aplicaciones/detalle.html', contexto)

def listar_vinilos(request):
    busqueda = request.GET.get("buscar")
    v=Vinilo.objects.all()
    
    if busqueda:
        v = Vinilo.objects.filter(
            Q(nombre_cantante__icontains = busqueda) |
            Q(nombre_vinilo__icontains = busqueda) |
            Q(estilo__icontains = busqueda)
            
        ).distinct()
    return render(request, 'aplicaciones/iniciocliente.html',{'v':v})

def listar_vinilos_vini(request):
    busqueda = request.GET.get("buscar")
    v=Vinilo.objects.all()
    
    if busqueda:
        v = Vinilo.objects.filter(
            Q(nombre_cantante__icontains = busqueda) |
            Q(nombre_vinilo__icontains = busqueda) |
            Q(estilo__icontains = busqueda)
            
        ).distinct()
    return render(request,'aplicaciones/viniloscli.html',{'v':v})

def cliente(request):
    cli=Cliente.objects.all()
    
    contexto={
        "cli":cli,
    }
    return render(request,'aplicaciones/cliente.html',contexto)

# def vin_pop(request, estilo):
#     v=get_object_or_404(Vinilo,id=estilo)
    
#     contexto={
#         "v":v,
#     }
#     return render(request, 'aplicaciones/vin_pop.html', contexto)