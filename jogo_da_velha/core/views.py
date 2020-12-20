from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
#from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Tabuleiro, User
from .form_user import UserForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def home(request):
    return render(request, 'index.html')


def submit_login(request):
    if request.POST:
        nome = request.POST.get('usuario')
        senha = request.POST.get('senha')
        usuario = authenticate(username=nome, password=senha)
        print(usuario)
        if usuario:
            login(request, usuario)
        else:
            messages.error(request, "Usuario ou Senha Invalidos")  #  retorna em caso da autenticação falhar
    return redirect('/')

def login_usuario(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login/')
def lista_tabuleiros(request):
    tabuleiros = Tabuleiro.objects.all()
    dados = {'tabuleiros': tabuleiros}
    return render(request, 'tabuleiros.html', dados)

@login_required(login_url='/login/')
def tabuleiro(request, id_tabuleiro):
    dados = {}
    dados['tabuleiro'] = Tabuleiro.objects.get(id=id_tabuleiro)
    return render(request, 'tabuleiro.html', dados)


def registra_usuario(request):
    form = UserForm()
    dados = {'form': form}
    if request.GET:
        return render(request, 'register.html', dados)
    elif request.POST:
        user = User.objects.create_user(request.POST.get('username'),
                                                 request.POST.get('email'),
                                                 request.POST.get('password'))
        dados['form'] = user
        #print(dados[form])
        return redirect("/")
    else:
        return render(request, 'register.html', dados)