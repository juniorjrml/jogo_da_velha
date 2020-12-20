from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Tabuleiro, User
from .form_user import UserForm


def home(request):
    return render(request, 'index.html')

def lista_tabuleiros(request):
    tabuleiros = Tabuleiro.objects.all()
    dados = {'tabuleiros': tabuleiros}
    return render(request, 'tabuleiros.html', dados)

def registra_usuario(request):
    form = UserForm()
    dados = {'form': form}
    if request.GET:
        return render(request, 'login.html', dados)
    elif request.POST:
        user = User.objects.create_user(request.POST.get('username'),
                                                 request.POST.get('email'),
                                                 request.POST.get('password'))

        dados['form'] = user
        #print(dados[form])
        return redirect("/")
    else:
        return render(request, 'login.html', dados)