# Generated by Django 3.1.4 on 2020-12-19 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201219_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabuleiro',
            name='tempo_ultima_jogada',
            field=models.DateField(blank=True, null=True, verbose_name='Ultima Jogada'),
        ),
    ]
