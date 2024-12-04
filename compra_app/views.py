from django.shortcuts import render, redirect
from .models import Compra

def inicio_vistaCompras(request):
    lasCompras = Compra.objects.all()
    return render(request, "gestionarCompras.html", {"misCompras": lasCompras})

def registrarCompra(request):
    id_compra = request.POST["numId_compra"]
    cantidad = request.POST["numCantidad"]
    fecha_compra = request.POST["txtFecha_compra"]
    forma_pago = request.POST["txtForma_pago"]
    total = request.POST["numTotal"]
    id_producto = request.POST["numId_producto"]
    id_encargo = request.POST["numId_encargo"]

    Compra.objects.create(
        id_compra=id_compra,
        cantidad=cantidad,
        fecha_compra=fecha_compra,
        forma_pago=forma_pago,
        total=total,
        id_producto=id_producto,
        id_encargo=id_encargo,
    )

    return redirect("compras")

def seleccionarCompra(request, id_compra):
    compra = Compra.objects.get(id_compra=id_compra)
    return render(request, "editarCompras.html", {"misCompras": compra})

def editarCompra(request):
    id_compra = request.POST["numId_compra"]
    cantidad = request.POST["numCantidad"]
    fecha_compra = request.POST["txtFecha_compra"]
    forma_pago = request.POST["txtForma_pago"]
    total = request.POST["numTotal"]
    id_producto = request.POST["numId_producto"]
    id_encargo = request.POST["numId_encargo"]

    compra = Compra.objects.get(id_compra=id_compra)
    compra.cantidad = cantidad
    compra.fecha_compra = fecha_compra
    compra.forma_pago = forma_pago
    compra.total = total
    compra.id_producto = id_producto
    compra.id_encargo = id_encargo
    compra.save()

    return redirect("compras")

def borrarCompra(request, id_compra):
    compra = Compra.objects.get(id_compra=id_compra)
    compra.delete()
    return redirect("compras")
