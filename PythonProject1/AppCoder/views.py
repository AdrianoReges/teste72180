from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import Context, Template

from .models import Estudante

def lista_estudantes(request):
    estudantes = Estudante.objects.all()
    return render(request, 'AppCoder/estudantes_list.html', {'estudantes': estudantes})

def detalhe_estudante(request, pk):
    estudante = get_object_or_404(Estudante, pk=pk)
    return render(request, 'AppCoder/estudante_detail.html', {'estudante': estudante})


def home(request):
    return render(request, 'AppCoder/home.html')
