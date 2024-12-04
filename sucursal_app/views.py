from django.shortcuts import render, redirect
from .models import Sucursal

# Vista inicial para listar las sucursales
def inicio_vistaSucursales(request):
    lasSucursales = Sucursal.objects.all()
    return render(request, "gestionarSucursales.html", {"misSucursales": lasSucursales})

# Registrar una nueva sucursal
def registrarSucursal(request):
    id_sucursal = request.POST["numID_sucursal"]
    nombre = request.POST["txtNombre"]
    direccion = request.POST["txtDireccion"]
    telefono = request.POST["numTelefono"]
    ciudad = request.POST["txtCiudad"]
    estado = request.POST["txtEstado"]
    codigo_postal = request.POST["numCodigoPostal"]

    Sucursal.objects.create(
        id_sucursal=id_sucursal,
        nombre=nombre,
        direccion=direccion,
        telefono=telefono,
        ciudad=ciudad,
        estado=estado,
        codigo_postal=codigo_postal
    )
    return redirect("sucursales")

# Seleccionar sucursal para edición
def seleccionarSucursal(request, id_sucursal):
    sucursal = Sucursal.objects.get(id_sucursal=id_sucursal)
    return render(request, "editarSucursal.html", {"misSucursales": sucursal})

# Editar los datos de una sucursal
def editarSucursal(request):
    id_sucursal = request.POST["numID_sucursal"]
    nombre = request.POST["txtNombre"]
    direccion = request.POST["txtDireccion"]
    telefono = request.POST["numTelefono"]
    ciudad = request.POST["txtCiudad"]
    estado = request.POST["txtEstado"]
    codigo_postal = request.POST["numCodigoPostal"]

    sucursal = Sucursal.objects.get(id_sucursal=id_sucursal)
    sucursal.nombre = nombre
    sucursal.direccion = direccion
    sucursal.telefono = telefono
    sucursal.ciudad = ciudad
    sucursal.estado = estado
    sucursal.codigo_postal = codigo_postal
    sucursal.save()
    return redirect("sucursales")

# Borrar una sucursal
def borrarSucursal(request, id_sucursal):
    sucursal = Sucursal.objects.get(id_sucursal=id_sucursal)
    sucursal.delete()
    return redirect("sucursales")