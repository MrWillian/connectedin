# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-29 23:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0003_auto_20200329_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='usuario',
        ),
        migrations.AddField(
            model_name='perfil',
            name='email',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]