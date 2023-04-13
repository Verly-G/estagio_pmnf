from django.shortcuts import render

def index(request):
    context = {
        'titulo':'Sistema de Estágio',
    }
    return render(request, 'estagio/index.html', context)