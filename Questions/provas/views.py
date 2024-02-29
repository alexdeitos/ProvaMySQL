from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Pergunta, Prova
from .forms import ProvaSelectForm
import random


def index(request):
    if request.method == 'POST':
        form = ProvaSelectForm(request.POST)
        if form.is_valid():
            prova_id = form.cleaned_data['prova'].id
            url = reverse('exibir_prova', args=[prova_id])
            return redirect(url)
    else:
        form = ProvaSelectForm()

    return render(request, 'index.html', {'form': form})

"""
def exibir_prova(request, prova_id):
    prova = Prova.objects.get(id=prova_id)
    perguntas = Pergunta.objects.filter(prova=prova)
    return render(request, 'exibir_prova.html', {'prova': prova, 'perguntas': perguntas})
"""
def exibir_prova(request, prova_id):
    prova = Prova.objects.get(id=prova_id)
    perguntas = prova.pergunta_set.all().order_by('?')  # Ordena as perguntas de forma aleatória

    context = {
        'prova': prova,
        'perguntas': perguntas,
    }

    return render(request, 'exibir_prova.html', context)