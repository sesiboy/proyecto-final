from django.shortcuts import render, redirect
from .models import Producto

# Página inicial con lista de productos
def inicio_vistaProductos(request):
    losProductos = Producto.objects.all()
    return render(request, "gestionarProductos.html", {"misProductos": losProductos})

# Registrar un producto nuevo
def registrarProducto(request):
    id_producto = request.POST["numID_producto"]
    nombre = request.POST["txtNombre"]
    categoria = request.POST["txtCategoria"]
    precio = request.POST["numPrecio"]
    cantidad_disponible = request.POST["numCantidad"]
    fecha_vencimiento = request.POST["fechaVencimiento"]
    id_distribuidor = request.POST["numID_distribuidor"]
    id_sucursal = request.POST["numID_sucursal"]

    Producto.objects.create(
        id_producto=id_producto,
        nombre=nombre,
        categoria=categoria,
        precio=precio,
        cantidad_disponible=cantidad_disponible,
        fecha_vencimiento=fecha_vencimiento,
        id_distribuidor=id_distribuidor,
        id_sucursal=id_sucursal,
    )

    return redirect("productos")

# Seleccionar un producto para editar
def seleccionarProducto(request, id_producto):
    producto = Producto.objects.get(id_producto=id_producto)
    return render(request, "editarProducto.html", {"misProductos": producto})

# Editar un producto existente
def editarProducto(request):
    id_producto = request.POST["numID_producto"]
    nombre = request.POST["txtNombre"]
    categoria = request.POST["txtCategoria"]
    precio = request.POST["numPrecio"]
    cantidad_disponible = request.POST["numCantidad"]
    fecha_vencimiento = request.POST["fechaVencimiento"]
    id_distribuidor = request.POST["numID_distribuidor"]
    id_sucursal = request.POST["numID_sucursal"]

    producto = Producto.objects.get(id_producto=id_producto)
    producto.nombre = nombre
    producto.categoria = categoria
    producto.precio = precio
    producto.cantidad_disponible = cantidad_disponible
    producto.fecha_vencimiento = fecha_vencimiento
    producto.id_distribuidor = id_distribuidor
    producto.id_sucursal = id_sucursal
    producto.save()

    return redirect("productos")

# Borrar un producto
def borrarProducto(request, id_producto):
    producto = Producto.objects.get(id_producto=id_producto)
    producto.delete()
    return redirect("productos")
