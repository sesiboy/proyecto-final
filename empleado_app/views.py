from django.shortcuts import render, redirect
from .models import Empleados
# Create your views here.
def inicio_vistaEmpleados(request):
    losEmpleados=Empleados.objects.all()
    return render(request,"gestionarEmpleados.html", {"misEmpleados":losEmpleados}   )

def registrarEmpleados(request):
    ID_empleado=request.POST["numID_empleado"]
    Nombre=request.POST["txtNombre"]
    Puesto=request.POST["txtPuesto"]
    Sueldo=request.POST["numSueldo"]
    Telefono=request.POST["numTelefono"]
    Fecha_nac=request.POST["datFecha_nac"]
    Genero=request.POST["txtGenero"]
    
    guardarEmpleados=Empleados.objects.create(
        ID_empleado=ID_empleado,Nombre=Nombre,Puesto=Puesto,Sueldo=Sueldo,Telefono=Telefono,Fecha_nac=Fecha_nac,Genero=Genero
    ) #GUARDA EL REGISTRO
    
    return redirect("empleados")

def seleccionarEmpleados(request,ID_empleado):
    empleados=Empleados.objects.get(ID_empleado=ID_empleado)
    return render(request, "editarEmpleados.html",{"misEmpleados":empleados})

def editarEmpleados(request):
    ID_empleado=request.POST["numID_empleado"]
    Nombre=request.POST["txtNombre"]
    Puesto=request.POST["txtPuesto"]
    Sueldo=request.POST["numSueldo"]
    Telefono=request.POST["numTelefono"]
    Fecha_nac=request.POST["datFecha_nac"]
    Genero=request.POST["txtGenero"]
    empleados=Empleados.objects.get(ID_empleado=ID_empleado)
    empleados.Nombre=Nombre
    empleados.Puesto=Puesto
    empleados.Sueldo=Sueldo
    empleados.Telefono=Telefono
    empleados.Fecha_nac=Fecha_nac
    empleados.Genero=Genero
    
    empleados.save() #guarda registro actualizado
    return redirect("empleados")

def borrarEmpleados(request,ID_empleado):
    empleados=Empleados.objects.get(ID_empleado=ID_empleado)
    empleados.delete() # borra el registro
    return redirect("empleados")