from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
#from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Tabuleiro, User
from .form_user import UserForm
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta


@login_required(login_url='/login/')
def home(request):
    return render(request, 'index.html')


def submit_login(request):
    if request.POST:
        nome = request.POST.get('usuario')
        senha = request.POST.get('senha')
        usuario = authenticate(username=nome, password=senha)
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


@login_required(login_url='/login/')
def registrar_jg(request, id_tabuleiro):
    dados = {}
    user = request.user
    dados['tabuleiro'] = Tabuleiro.objects.get(id=id_tabuleiro)

    if not dados['tabuleiro'].jogador1:
        if dados['tabuleiro'].jogador2 != user:
            dados['tabuleiro'].jogador1 = user
    elif not dados['tabuleiro'].jogador2:
        if dados['tabuleiro'].jogador1 != user:
            dados['tabuleiro'].jogador2 = user
    dados['tabuleiro'].save()

    return render(request, 'tabuleiro.html', dados)

@login_required(login_url='/login/')
def abandonar_jg(request, id_tabuleiro):
    dados = {}
    user = request.user
    dados['tabuleiro'] = Tabuleiro.objects.get(id=id_tabuleiro)

    if dados['tabuleiro'].jogador1 == user:
        dados['tabuleiro'].jogador1 = None
    elif dados['tabuleiro'].jogador2 == user:
        dados['tabuleiro'].jogador2 = None
    dados['tabuleiro'].finalizar_jogo()
    dados['tabuleiro'].save()

    return render(request, 'tabuleiro.html', dados)

@login_required(login_url='/login/')
def registrar_jogada(request, id_tabuleiro, casa):
    dados = {}
    tabuleiro = Tabuleiro.objects.get(id=id_tabuleiro)
    tabuleiro.registrar_movimento(casa)
    tabuleiro.troca_vez_jogador()

    print(tabuleiro.e_jogada_atrasado())

    dados['tabuleiro'] = tabuleiro

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