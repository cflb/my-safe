"""
   Views to myapp
"""

from rest_framework import viewsets
from .models import Ambiente, Aplicacao, Segredo
from .serializers import AmbienteSerializer, AplicacaoSerializer, SegredoSerializer

class AmbienteViewSet(viewsets.ModelViewSet):
    """
    class AmbienteViewSet.
        to provide a view to model.
    """
    queryset = Ambiente.objects.all()
    serializer_class = AmbienteSerializer

class AplicacaoViewSet(viewsets.ModelViewSet):
    """
    class AplicacaoViewSet.
        to provide a view to model.
    """
    queryset = Aplicacao.objects.all()
    serializer_class = AplicacaoSerializer

class SegredoViewSet(viewsets.ModelViewSet):
    """
    class SegredoViewSet.
        to provide a view to model.
    """
    queryset = Segredo.objects.all()
    serializer_class = SegredoSerializer
