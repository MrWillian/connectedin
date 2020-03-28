# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Perfil(models.Model):
  
  nome = models.CharField(max_length=255, null=False)
  email = models.CharField(max_length=255, null=False)
  telefone = models.CharField(max_length=15, null=False)
  nome_empresa = models.CharField(max_length=255, null=False)

  def convidar(self, perfil_convidado):
    pass

class Convite(models.Model):
  
  solicitante = models.ForeignKey(Perfil, related_name='convites_feitos')
  convidado = models.ForeignKey(Perfil, related_name='convites_recebidos')
