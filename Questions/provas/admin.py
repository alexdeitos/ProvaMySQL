from django.contrib import admin
from .models import Pergunta, Resposta

class RespostaInline(admin.TabularInline):
    model = Resposta
    extra = 4

class PerguntaAdmin(admin.ModelAdmin):
    inlines = [RespostaInline]
    
    # Adicione uma barra de pesquisa para procurar pelo ID da pergunta
    search_fields = ['id', 'texto']
    
    # Liste as perguntas com os campos ID e texto da pergunta
    list_display = ['id', 'texto']

admin.site.register(Pergunta, PerguntaAdmin)


"""
from django.contrib import admin
from .models import Pergunta, Resposta

class RespostaInline(admin.TabularInline):
    model = Resposta
    extra = 4

class PerguntaAdmin(admin.ModelAdmin):
    inlines = [RespostaInline]
#    ordering = ['id']  # Ordena pelo campo 'id', que representa a ordem de criação

admin.site.register(Pergunta, PerguntaAdmin)
"""