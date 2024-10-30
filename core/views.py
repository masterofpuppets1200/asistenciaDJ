from django.shortcuts import render
from rest_framework import generics
from .models import usuarioAlum,usuarioPro
from .serializers import usuarioAlumSerializer,usuarioProSerializer

# Create your views here.

class usuarioAlumViewSet(generics.ListAPIView):
    queryset = usuarioAlum.objects.all()
    serializer_class = usuarioAlumSerializer
    
class usuarioProViewSet(generics.ListAPIView):
    queryset = usuarioPro.objects.all()
    serializer_class = usuarioProSerializer