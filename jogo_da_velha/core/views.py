from django.shortcuts import render
from .models import Tabuleiro
from .form_user import UserForm

def home(request):
    return render(request, 'index.html')

def lista_tabuleiros(request):
    tabuleiros = Tabuleiro.objects.all()
    dados = {'tabuleiros': tabuleiros}
    return render(request, 'tabuleiros.html', dados)

def registra_usuario(request):
    if request.GET:
        form = UserForm()
        dados = {'form': form}
        return  render(request, 'login.html', dados)
    elif request.POST:
        pass