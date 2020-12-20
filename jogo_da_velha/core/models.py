from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tabuleiro(models.Model):
    nome = models.CharField(max_length=100)
    jogador1 = models.ForeignKey(User, related_name='jogador1', blank=True, null=True, on_delete=models.SET_NULL)
    jogador2 = models.ForeignKey(User, related_name='jogador2', blank=True, null=True, on_delete=models.SET_NULL)
    jogador_da_vez = models.ForeignKey(User, related_name='jogador_da_vez', blank=True, null=True, on_delete=models.SET_NULL)
    tempo_ultima_jogada = models.DateField(verbose_name="Ultima Jogada",null=True, blank=True)
    casa1 = models.IntegerField()
    casa2 = models.IntegerField()
    casa3 = models.IntegerField()
    casa4 = models.IntegerField()
    casa5 = models.IntegerField()
    casa6 = models.IntegerField()
    casa7 = models.IntegerField()
    casa8 = models.IntegerField()
    casa9 = models.IntegerField()

    def __str__(self):
        return self.nome