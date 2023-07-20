from django.contrib import admin
from .models import Pergunta, Resposta, Prova


class RespostaInline(admin.TabularInline):
    model = Resposta
    extra = 4


class PerguntaAdmin(admin.ModelAdmin):
    inlines = [RespostaInline]


admin.site.register(Pergunta, PerguntaAdmin)
admin.site.register(Prova)

