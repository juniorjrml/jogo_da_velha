# Generated by Django 3.1.4 on 2020-12-19 20:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabuleiro',
            name='jogador1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='jogador1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tabuleiro',
            name='jogador2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='jogador2', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tabuleiro',
            name='jogador_da_vez',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='jogador_da_vez', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tabuleiro',
            name='tempo_ultima_jogada',
            field=models.DateField(blank=True, verbose_name='Ultima Jogada'),
        ),
    ]
