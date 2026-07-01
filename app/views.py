from django.shortcuts import render
from .models import Sobre,Autora, Elenco

def index(request):
    return render(request, "index.html")

def sobre(request):
    informacoes = Sobre.objects.all()

    return render(request, 'sobre.html', {
        'informacoes' : informacoes
    })

def elenco(request):

    personagens = Elenco.objects.all()

    return render(request, 'elenco.html', {
        'personagens': personagens
    })

def autoras(request):
    autoras = Autora.objects.all()

    return render(request, 'autoras.html', {
        'autoras': autoras
    })