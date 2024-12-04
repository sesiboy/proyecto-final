from django.shortcuts import render, redirect
from .models import Venta

# Mostrar lista de ventas
def inicio_vistaVenta(request):
    lasVentas = Venta.objects.all()
    return render(request, "gestionarVenta.html", {"misVentas": lasVentas})

# Registrar una nueva venta
def registrarVenta(request):
    id_venta = request.POST["numID_venta"]
    id_empleado = request.POST["numID_empleado"]
    id_cliente = request.POST["numID_cliente"]
    id_producto = request.POST["numID_producto"]
    id_sucursal = request.POST["numID_sucursal"]
    fecha = request.POST["fechaVenta"]
    total = request.POST["numTotal"]

    Venta.objects.create(
        id_venta=id_venta,
        id_empleado=id_empleado,
        id_cliente=id_cliente,
        id_producto=id_producto,
        id_sucursal=id_sucursal,
        fecha=fecha,
        total=total
    )
    return redirect("venta")

# Seleccionar venta para editar
def seleccionarVenta(request, id_venta):
    venta = Venta.objects.get(id_venta=id_venta)
    return render(request, "editarVenta.html", {"venta": venta})

# Editar una venta existente
def editarVenta(request):
    id_venta = request.POST["numID_venta"]
    id_empleado = request.POST["numID_empleado"]
    id_cliente = request.POST["numID_cliente"]
    id_producto = request.POST["numID_producto"]
    id_sucursal = request.POST["numID_sucursal"]
    fecha = request.POST["fechaVenta"]
    total = request.POST["numTotal"]

    venta = Venta.objects.get(id_venta=id_venta)
    venta.id_empleado = id_empleado
    venta.id_cliente = id_cliente
    venta.id_producto = id_producto
    venta.id_sucursal = id_sucursal
    venta.fecha = fecha
    venta.total = total
    venta.save()

    return redirect("venta")

# Borrar una venta
def borrarVenta(request, id_venta):
    venta = Venta.objects.get(id_venta=id_venta)
    venta.delete()
    return redirect("venta")
