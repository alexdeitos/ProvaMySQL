from django.contrib import admin
from .models import Pergunta, Resposta, Prova

class RespostaInline(admin.TabularInline):
    model = Resposta
    extra = 4

class PerguntaAdmin(admin.ModelAdmin):
    inlines = [RespostaInline]
    search_fields = ['id', 'texto']
    list_display = ['get_nome_prova', 'texto']
    ordering = ['prova__nome', 'id']  # Adicionando ordenação por nome da prova e ID

    def get_nome_prova(self, obj):
        return obj.prova.nome

    get_nome_prova.short_description = 'Nome da Prova'

admin.site.register(Pergunta, PerguntaAdmin)
admin.site.register(Prova)

