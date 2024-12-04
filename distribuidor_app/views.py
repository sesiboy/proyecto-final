from django.shortcuts import render, redirect
from .models import Distribuidor

# Vista inicial para listar los distribuidores
def inicio_vistaDistribuidores(request):
    losDistribuidores = Distribuidor.objects.all()
    return render(request, "gestionarDistribuidores.html", {"misDistribuidores": losDistribuidores})

# Registrar un nuevo distribuidor
def registrarDistribuidor(request):
    id_distribuidor = request.POST["numID_distribuidor"]
    nombre = request.POST["txtNombre"]
    telefono = request.POST["numTelefono"]
    direccion = request.POST["txtDireccion"]
    ciudad = request.POST["txtCiudad"]
    estado = request.POST["txtEstado"]
    productos_distribuidos = request.POST["txtProductosDistribuidos"]

    Distribuidor.objects.create(
        id_distribuidor=id_distribuidor,
        nombre=nombre,
        telefono=telefono,
        direccion=direccion,
        ciudad=ciudad,
        estado=estado,
        productos_distribuidos=productos_distribuidos
    )
    return redirect("distribuidores")

# Seleccionar distribuidor para edición
def seleccionarDistribuidor(request, id_distribuidor):
    distribuidor = Distribuidor.objects.get(id_distribuidor=id_distribuidor)
    return render(request, "editarDistribuidor.html", {"misDistribuidores": distribuidor})

# Editar los datos de un distribuidor
def editarDistribuidor(request):
    id_distribuidor = request.POST["numID_distribuidor"]
    nombre = request.POST["txtNombre"]
    telefono = request.POST["numTelefono"]
    direccion = request.POST["txtDireccion"]
    ciudad = request.POST["txtCiudad"]
    estado = request.POST["txtEstado"]
    productos_distribuidos = request.POST["txtProductosDistribuidos"]

    distribuidor = Distribuidor.objects.get(id_distribuidor=id_distribuidor)
    distribuidor.nombre = nombre
    distribuidor.telefono = telefono
    distribuidor.direccion = direccion
    distribuidor.ciudad = ciudad
    distribuidor.estado = estado
    distribuidor.productos_distribuidos = productos_distribuidos
    distribuidor.save()
    return redirect("distribuidores")

# Borrar un distribuidor
def borrarDistribuidor(request, id_distribuidor):
    distribuidor = Distribuidor.objects.get(id_distribuidor=id_distribuidor)
    distribuidor.delete()
    return redirect("distribuidores")
