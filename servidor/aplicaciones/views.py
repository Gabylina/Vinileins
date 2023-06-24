from django.shortcuts import render,get_object_or_404,redirect
from datetime import date
from .models import Administrador,Vinilo
from .forms import formCrearVinilo,formModificarVinilo
from django.db.models import Q
from django.contrib.auth.decorators import login_required #obliga a que este logeado el cliente para realizar el cambio de vista
# Create your views here.

def index(request):
    admin=Administrador.objects.all()
    
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
    vinilo=get_object_or_404(Vinilo,id=id)
    
    form=formCrearVinilo(request.POST,request.FILES or None,instance=vinilo)
    
    
    print(vinilo)
    print("#################")
    contexto={
        "vinilo":vinilo,
        "form":form,
        
    }
    
    if request.method=="POST":

        form=formModificarVinilo(data=request.POST and request.FILES,instance=vinilo)

        if form.is_valid():
            
            datos=form.cleaned_data
            mvinilo=Vinilo.objects.get(id=Vinilo.id)
            mvinilo.cara_delante=datos.get("cara_delante")
            mvinilo.cara_detras=datos.get("cara_detras")
            mvinilo.nombre_cantante=datos.get("nombre_cantante")
            mvinilo.nombre_vinilo=datos.get("nombre_vinilo")
            mvinilo.estilo=datos.get("estilo")
            mvinilo.precio=datos.get("precio")
            
            mvinilo.save()
            return redirect(to="vinilos")
        
    return render(request,'aplicaciones/modificarvinilo.html',contexto)

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

@login_required
def pagar_log_required(request):
    
    return render(request,'aplicaciones/pagar_log_required.html')

# def vin_pop(request, estilo):
#     v=get_object_or_404(Vinilo,id=estilo)
    
#     contexto={
#         "v":v,
#     }
#     return render(request, 'aplicaciones/vin_pop.html', contexto)