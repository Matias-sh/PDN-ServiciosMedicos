from django import forms
from django.forms import ModelForm
from .models import Pacientes

class FormPaciente(ModelForm):
    class Meta:
        
        model = Pacientes

        fields = '__all__'

        widgets = {
            'id_persona': forms.Select(attrs={'class': 'form-control'}),
            'sintomas': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Describa los sintomas del paciente'})
        }

        labels = {
            'id_persona': 'Datos de Persona:',
            'sintomas': 'Sintomas del Paciente:'
        }