from django.urls import path
from empleado_app import views
urlpatterns = [
    path("empleados", views.inicio_vistaEmpleados, name= "empleados" ),
    path("registrarEmpleados/",views.registrarEmpleados,name="registrarEmpleados"),
    path("seleccionarEmpleados/<ID_empleado>",views.seleccionarEmpleados,name="seleccionarEmpleados"),
    path("editarEmpleados/",views.editarEmpleados,name="editarEmpleados"),
    path("borrarEmpleados/<ID_empleado>",views.borrarEmpleados,name="borrarEmpleados")
]