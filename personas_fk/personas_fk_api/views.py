from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.

from .models import Persona, Genero, TipoEstudiante
from .serializers import PersonaSerializer, GeneroSerializer, TipoEstudianteSerializer


class PersonaView(viewsets.ModelViewSet):
    serializer_class = PersonaSerializer
    queryset = Persona.objects.all()


class TipoEstudianteView(viewsets.ModelViewSet):
    serializer_class = TipoEstudianteSerializer
    queryset = TipoEstudiante.objects.all()


class GeneroView(viewsets.ModelViewSet):
    serializer_class = GeneroSerializer
    queryset = Genero.objects.all()
