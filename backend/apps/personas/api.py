from rest_framework import viewsets, permissions
from .models import Personas
from .serializers import PersonasSerializers

class PersonasViewSet(viewsets.ModelViewSet):
    queryset = Personas.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PersonasSerializers
