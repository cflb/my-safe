# myapp/admin.py
from django.contrib import admin
from .models import Ambiente, Aplicacao, Segredo

@admin.register(Ambiente)
class AmbienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    
    def __str__(self):
        return self.nome

@admin.register(Aplicacao)
class AplicacaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'ambiente']

    def __str__(self):
        return self.ambiente

@admin.register(Segredo)
class SegredoAdmin(admin.ModelAdmin):
    list_display = ['id', 'chave', 'valor', 'aplicacao']

    def __str__(self):
        return self.aplicacao
