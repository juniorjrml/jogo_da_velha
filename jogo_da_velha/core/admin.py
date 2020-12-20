from django.contrib import admin
from .models import Tabuleiro
# Register your models here.

class TabuleiroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'jogador1', 'jogador2', 'tempo_ultima_jogada')

admin.site.register(Tabuleiro, TabuleiroAdmin)