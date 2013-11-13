#-*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from models import Company, Incident
from forms import IncidentForm


@login_required
def home(request):
    '''
    Dashboard
    '''
    company = Company.objects.get(users__pk=request.user.pk)
    return render(request, 'core/home.html', locals())


@login_required
def solicitations(request):
    '''
    Lista de solicitações
    '''
    company = Company.objects.get(users__pk=request.user.pk)
    incidents = Incident.objects.filter(company=company.pk).order_by('-date_open')
    return render(request, 'core/solicitations.html', locals())


@login_required
def solicitation_add(request):
    '''
    Adicionar solicitaçõe
    '''
    company = Company.objects.get(users__pk=request.user.pk)

    if request.method == 'POST':
        form = IncidentForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('core:solicitation-add')
    else:
        form = IncidentForm(initial={
            'company': company.pk,
            'requestor': request.user.pk
        })

    return render(request, 'core/solicitation_add.html', {
        'form': form
    })


@login_required
def settings(request):
    '''
    Configurações
    '''
    company = Company.objects.get(users__pk=request.user.pk)
    return render(request, 'core/settings.html', locals())