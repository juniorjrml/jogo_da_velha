from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth.models import User



class Tabuleiro(models.Model):
    nome = models.CharField(max_length=100)
    jogador1 = models.ForeignKey(User, related_name='jogador1', blank=True, null=True, on_delete=models.SET(None))
    jogador2 = models.ForeignKey(User, related_name='jogador2', blank=True, null=True, on_delete=models.SET(None))
    jogador_da_vez = models.ForeignKey(User, related_name='jogador_da_vez', blank=True, null=True, on_delete=models.SET(None))
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

    def get_jogador1(self):
        return self.jogador1

    def get_jogador2(self):
        return self.jogador2

    def tem_vaga(self):
        if self.jogador1 != None and self.jogador2 != None:
            return False
        else:
            return True

    def iniciar_jogo(self):
        self.finalizar_jogo()
        self.jogador_da_vez = self.jogador1
        self.tempo_ultima_jogada = datetime.now()
        self.save()

    def get_jogador_da_vez(self):
        if self.jogador_da_vez == self.jogador1:
            return 1
        elif self.jogador_da_vez == self.jogador2:
            return 2
        else:
            return 0


    def get_tempo_ultima_jogada(self):
        return self.tempo_ultima_jogada


    def e_jogada_atrasado(self):
        data = self.tempo_ultima_jogada + timedelta(seconds=5)
        if datetime.now().date() > data:
            return True
        else:
            return False


    def finalizar_jogo(self):
        self.casa1 = 0
        self.casa2 = 0
        self.casa3 = 0
        self.casa4 = 0
        self.casa5 = 0
        self.casa6 = 0
        self.casa7 = 0
        self.casa8 = 0
        self.casa9 = 0
        self.jogador_da_vez = None
        self.tempo_ultima_jogada = None
        self.save()



    def registrar_movimento(self, casa):
        if casa == 1:
            if self.casa1 == 0:
                self.casa1 = self.get_jogador_da_vez()
        elif casa == 2:
            if self.casa2 == 0:
                self.casa2 = self.get_jogador_da_vez()
        elif casa == 3:
            if self.casa3 == 0:
                self.casa3 = self.get_jogador_da_vez()
        elif casa == 4:
            if self.casa4 == 0:
                self.casa4 = self.get_jogador_da_vez()
        elif casa == 5:
            if self.casa5 == 0:
                self.casa5 = self.get_jogador_da_vez()
        elif casa == 6:
            if self.casa6 == 0:
                self.casa6 = self.get_jogador_da_vez()
        elif casa == 7:
            if self.casa7 == 0:
                self.casa7 = self.get_jogador_da_vez()
        elif casa == 8:
            if self.casa8 == 0:
                self.casa8 = self.get_jogador_da_vez()
        else:
            if self.casa9 == 0:
                self.casa9 = self.get_jogador_da_vez()
        #self.tempo_ultima_jogada = datetime.now().date()
        self.save()


    def troca_vez_jogador(self):
        if self.get_jogador_da_vez() == 1:
            self.jogador_da_vez = self.jogador2
        elif self.get_jogador_da_vez() == 2:
            self.jogador_da_vez = self.jogador1
        else:
            self.finalizar_jogo()
        self.save()
