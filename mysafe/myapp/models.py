"""
    Models to myapp
"""

from django.db import models

class Ambiente(models.Model):
    """
    class Ambiente.
        to provide a data model
    """
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Aplicacao(models.Model):
    """
    class Aplicacao.
        to provide a data model.
    """
    nome = models.CharField(max_length=255)
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE, related_name='aplicacoes')

    def __str__(self):
        return str(self.ambiente)

class Segredo(models.Model):
    """
    class Segredo.
        to provide a data model.
    """
    chave = models.CharField(max_length=255)
    valor = models.CharField(max_length=255)
    aplicacao = models.ForeignKey(Aplicacao, on_delete=models.CASCADE, related_name='segredos')

    def __str__(self):
        return str(self.aplicacao)
