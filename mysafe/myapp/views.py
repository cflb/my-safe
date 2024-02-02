# myapp/views.py
from rest_framework import viewsets
from .models import Ambiente, Aplicacao, Segredo
from .serializers import AmbienteSerializer, AplicacaoSerializer, SegredoSerializer

class AmbienteViewSet(viewsets.ModelViewSet):
    queryset = Ambiente.objects.all()
    serializer_class = AmbienteSerializer

class AplicacaoViewSet(viewsets.ModelViewSet):
    queryset = Aplicacao.objects.all()
    serializer_class = AplicacaoSerializer

class SegredoViewSet(viewsets.ModelViewSet):
    queryset = Segredo.objects.all()
    serializer_class = SegredoSerializer
