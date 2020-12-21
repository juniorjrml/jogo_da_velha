"""jogo_da_velha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.urls import urlpatterns
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('tabuleiros', views.lista_tabuleiros),
    path('tabuleiro/<int:id_tabuleiro>', views.tabuleiro),
    path('tabuleiro/registrajogador/<int:id_tabuleiro>', views.registrar_jg),
    path('tabuleiro/abandonar/<int:id_tabuleiro>', views.abandonar_jg),
    path('tabuleiro/jogada/<int:id_tabuleiro>/<int:casa>', views.registrar_jogada),
    path('tabuleiro/atualizar/<int:id_tabuleiro>/', views.atualiza),
    path('usuario/register', views.registra_usuario),
    path('login/', views.login_usuario),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user)
]

