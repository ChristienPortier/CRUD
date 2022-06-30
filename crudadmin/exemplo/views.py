from django.shortcuts import render


# Create your views here.
from exemplo.models import Cliente

def index(request):
    lista = Cliente.objects.all()
    context = {
        'lista' : lista,
    }
    return render(request, 'index.html', context)