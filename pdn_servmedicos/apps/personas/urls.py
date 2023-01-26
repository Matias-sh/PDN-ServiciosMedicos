from django.urls import path
from .views import *

urlpatterns = [
    path('', vista_personas, name='vista_personas'),
    path('nueva_persona/', vista_nueva_persona, name='nueva_persona'),
    path('editar_persona/<int:id>/', vista_editar_persona, name='editar_persona'),
    path('eliminar_persona/<int:id>/', vista_eliminar_persona, name='eliminar_persona'),
]