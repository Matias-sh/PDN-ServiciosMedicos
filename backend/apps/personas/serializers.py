from rest_framework import serializers
from .models import Personas

class PersonasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Personas
        fields = (
            'nombre',
            'apellido',
            'edad',
            'telefono',
            'email',
            'domicilio'
        )
