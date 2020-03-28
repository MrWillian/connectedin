# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-28 17:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Convite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=15)),
                ('nome_empresa', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='convite',
            name='convidado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='convites_recebidos', to='perfis.Perfil'),
        ),
        migrations.AddField(
            model_name='convite',
            name='solicitante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='convites_feitos', to='perfis.Perfil'),
        ),
    ]