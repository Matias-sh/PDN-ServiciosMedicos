from django.db import models
from apps.personas.models import Personas

# Create your models here.

class Pacientes(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    sintomas = models.TextField()
    id_persona = models.ForeignKey(Personas, on_delete=models.CASCADE)
