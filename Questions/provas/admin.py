from django.contrib import admin
from .models import Pergunta, Resposta

class RespostaInline(admin.TabularInline):
    model = Resposta
    extra = 4

class PerguntaAdmin(admin.ModelAdmin):
    inlines = [RespostaInline]
    ordering = ['id']  # Ordena pelo campo 'id', que representa a ordem de criação

admin.site.register(Pergunta, PerguntaAdmin)

