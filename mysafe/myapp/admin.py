"""
ADMIN interface for myapp.
"""
from django.contrib import admin
from .models import Ambiente, Aplicacao, Segredo

@admin.register(Ambiente)
class AmbienteAdmin(admin.ModelAdmin):
    """
    class AmbienteAdmin.
        to provide to interface admin to Ambiente model
    """
    list_display = ['id', 'nome']

    def __str__(self):
        return self.nome

@admin.register(Aplicacao)
class AplicacaoAdmin(admin.ModelAdmin):
    """
    class AplicacaoAdmin.
        to provide to interface admin to AplicacaoAdmin model
    """
    list_display = ['id', 'nome', 'ambiente']

    def __str__(self):
        return self.ambiente

@admin.register(Segredo)
class SegredoAdmin(admin.ModelAdmin):
    """
    class SegredoAdmin.
        to provide to interface admin to SegredoAdmin model
    """
    list_display = ['id', 'chave', 'valor', 'aplicacao']

    def __str__(self):
        return self.aplicacao
