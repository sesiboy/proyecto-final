from django.shortcuts import render, redirect
from .models import Cliente

# Vista inicial para listar los clientes
def inicio_vistaClientes(request):
    losClientes = Cliente.objects.all()
    return render(request, "gestionarClientes.html", {"misClientes": losClientes})

# Registrar un nuevo cliente
def registrarCliente(request):
    id_cliente = request.POST["numID_cliente"]
    nombre = request.POST["txtNombre"]
    correo = request.POST["txtCorreo"]
    telefono = request.POST["numTelefono"]
    direccion = request.POST["txtDireccion"]
    ciudad = request.POST["txtCiudad"]
    estado = request.POST["txtEstado"]

    Cliente.objects.create(
        id_cliente=id_cliente,
        nombre=nombre,
        correo=correo,
        telefono=telefono,
        direccion=direccion,
        ciudad=ciudad,
        estado=estado
    )
    return redirect("clientes")

# Seleccionar cliente para edición
def seleccionarCliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    return render(request, "editarCliente.html", {"misClientes": cliente})

# Editar los datos de un cliente
def editarCliente(request):
    id_cliente = request.POST["numID_cliente"]
    nombre = request.POST["txtNombre"]
    correo = request.POST["txtCorreo"]
    telefono = request.POST["numTelefono"]
    direccion = request.POST["txtDireccion"]
    ciudad = request.POST["txtCiudad"]
    estado = request.POST["txtEstado"]

    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.nombre = nombre
    cliente.correo = correo
    cliente.telefono = telefono
    cliente.direccion = direccion
    cliente.ciudad = ciudad
    cliente.estado = estado
    cliente.save()
    return redirect("clientes")

# Borrar un cliente
def borrarCliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.delete()
    return redirect("clientes")
