# myapp/serializers.py
from rest_framework import serializers
from .models import Ambiente, Aplicacao, Segredo

class AmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambiente
        fields = ['id', 'nome']

class AplicacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aplicacao
        fields = ['id', 'nome', 'ambiente']

class SegredoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segredo
        fields = ['id', 'chave', 'valor', 'aplicacao']
    

