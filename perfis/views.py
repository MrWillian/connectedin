# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from perfis.models import Perfil

def index(request):
  return render(request, 'index.html', {'perfis' : Perfil.objects.all()})

def exibir(request, perfil_id):
  print 'ID do perfil recebido: %s' % (perfil_id)
  perfil = Perfil.objects.get(id=perfil_id)
  return render(request, 'perfil.html', {"perfil" : perfil})

def convidar(request, perfil_id):
  pass
