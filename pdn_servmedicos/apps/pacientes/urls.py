from django.urls import path
from .views import *

urlpatterns = [
    path('', vista_pacientes, name="vista_pacientes"),
    path('nuevo_paciente/', vista_crear_paciente, name="crear_paciente"),
    path('editar_paciente/<int:id>/', vista_editar_paciente, name="editar_paciente"),
    path('eliminar_paciente/<int:id>/', vista_eliminar_paciente, name="eliminar_paciente")
]