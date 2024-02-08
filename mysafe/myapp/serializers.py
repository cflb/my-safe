"""
   Serializer to myapp
"""

from rest_framework import serializers
from .models import Ambiente, Aplicacao, Segredo

class AmbienteSerializer(serializers.ModelSerializer):
    """
    Serializer AmbienteSerializer.
        to provide a serializer data to model.
    """
    class Meta:
        model = Ambiente
        fields = ['id', 'nome']

class AplicacaoSerializer(serializers.ModelSerializer):
    """
    Serializer AplicacaoSerializer.
        to provide a serializer data to model.
    """
    class Meta:
        model = Aplicacao
        fields = ['id', 'nome', 'ambiente']

class SegredoSerializer(serializers.ModelSerializer):
    """
    Serializer SegredoSerializer.
        to provide a serializer data to model.
    """
    class Meta:
        model = Segredo
        fields = ['id', 'chave', 'valor', 'aplicacao']
