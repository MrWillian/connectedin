# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Peril(object):
  
  def __init__(self, nome='', email='', telefone='', nome_empresa=''):
    self.nome = nome
    self.email = email
    self.telefone = telefone
    self.nome_empresa = nome_empresa
    