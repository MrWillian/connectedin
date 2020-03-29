# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from perfis.models import Perfil, Convite
from django.contrib.auth.decorators import login_required

def index(request):
  return render(request, 'index.html', {'perfis' : Perfil.objects.all(), 'perfil_logado': get_perfil_logado(request) })

def exibir(request, perfil_id):
  perfil = Perfil.objects.get(id=perfil_id)
  perfil_logado = get_perfil_logado(request)
  is_contact = perfil in perfil_logado.contatos.all()
  return render(request, 'perfil.html', {"perfil" : perfil, "is_contact": is_contact})

def convidar(request, perfil_id):
  perfil_a_convidar = Perfil.objects.get(id=perfil_id)
  perfil_logado = get_perfil_logado(request)
  perfil_logado.convidar(perfil_a_convidar)
  return redirect('index')

def aceitar(request, convite_id):
  convite = Convite.objects.get(id=convite_id)
  convite.aceitar()
  return redirect('index')

def get_perfil_logado(request):
  return Perfil.objects.get(id=2)
