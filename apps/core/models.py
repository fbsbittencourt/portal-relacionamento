#-*- coding: utf-8 -*-

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Employee(models.Model):

    # personal data
    name = models.CharField(
        verbose_name='Nome',
        max_length=140
    )

    email = models.EmailField(
        verbose_name='E-mail'
    )

    phone = models.CharField(
        verbose_name='Telefone',
        max_length=14,
        blank=True,
        null=True
    )

    mobile_phone = models.CharField(
        verbose_name='Celular',
        max_length=14,
        blank=True,
        null=True
    )

    admission_date = models.DateField(
        verbose_name=u'DT Admissão'
    )

    # address
    street = models.CharField(
        verbose_name='Rua',
        max_length=75,
        blank=True,
        null=True
    )

    number = models.CharField(
        verbose_name='Número',
        max_length=12,
        blank=True,
        null=True
    )

    complement = models.CharField(
        verbose_name='Complemento',
        max_length=75,
        blank=True,
        null=True
    )

    neighborhood = models.CharField(
        verbose_name='Bairro',
        max_length=75,
        blank=True,
        null=True
    )

    # social networks
    facebook = models.URLField(
        verbose_name='Facebook',
        blank=True,
        null=True
    )

    twitter = models.URLField(
        verbose_name='Twitter',
        blank=True,
        null=True
    )

    linkedin = models.URLField(
        verbose_name='LinkedIn',
        blank=True,
        null=True
    )

    active = models.BooleanField(
        verbose_name='Registro Ativo',
        default=False
    )

    # Audit fields
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __unicode__(self):
        return self.name


class Company(models.Model):

    # personal data
    logo = models.ImageField(
        upload_to='logos',
        blank=True,
        null=True
    )

    name = models.CharField(
        'Razão Social',
        max_length=140
    )

    fancy_name = models.CharField(
        'Nome Fantasia',
        max_length=140
    )

    cnpj = models.CharField(
        'CNPJ',
        max_length=18
    )

    email = models.EmailField(
        'E-mail',
        blank=True,
        null=True
    )

    phone = models.CharField(
        'Telefone',
        max_length=14,
        blank=True,
        null=True
    )

    # address
    street = models.CharField(
        verbose_name='Rua',
        max_length=75,
        blank=True,
        null=True
    )

    number = models.CharField(
        verbose_name='Número',
        max_length=12,
        blank=True,
        null=True
    )

    complement = models.CharField(
        verbose_name='Complemento',
        max_length=75,
        blank=True,
        null=True
    )

    neighborhood = models.CharField(
        verbose_name='Bairro',
        max_length=75,
        blank=True,
        null=True
    )

    city = models.CharField(
        'Cidade',
        max_length=75,
        blank=True,
        null=True
    )

    users = models.ManyToManyField(
        User,
        verbose_name='Contatos',
        blank=True,
        null=True
    )

    # social networks
    facebook = models.URLField(
        verbose_name='Facebook',
        blank=True,
        null=True
    )

    twitter = models.URLField(
        verbose_name='Twitter',
        blank=True,
        null=True
    )

    linkedin = models.URLField(
        verbose_name='LinkedIn',
        blank=True,
        null=True
    )

    active = models.BooleanField(
        verbose_name='Registro Ativo',
        default=False
    )

    # Audit fields
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __unicode__(self):
        return self.fancy_name


class Incident(models.Model):

    PROGRESS = (
        (0,  '0%'),
        (10, '10%'),
        (20, '20%'),
        (30, '30%'),
        (40, '40%'),
        (50, '50%'),
        (60, '60%'),
        (70, '70%'),
        (80, '80%'),
        (90, '90%'),
        (100, 'Concluído'),
        (200, 'Cancelado'),
    )

    title = models.CharField(
        'Título',
        max_length=140
    )

    description = models.TextField(
        'Problema Relatado'
    )

    date_open = models.DateTimeField(
        'DT Abertura',
        default=datetime.now
    )

    date_final = models.DateTimeField(
        'DT Conclusão',
        blank=True,
        null=True
    )

    progress = models.PositiveSmallIntegerField(
        'Progresso',
        choices=PROGRESS
    )

    company = models.ForeignKey(
        'Company',
        verbose_name='Empresa',
    )

    requestor = models.ForeignKey(
        User,
        verbose_name='Solicitante'
    )

    responsible = models.ForeignKey(
        'Employee',
        verbose_name='Responsável',
        blank=True,
        null=True
    )

    # Audit fields
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Solicitação'
        verbose_name_plural = 'Solicitações'

    def __unicode__(self):
        return self.title


class Treatment(models.Model):

    incident = models.ForeignKey(
        'Incident'
    )

    description = models.TextField(
        'Serviço realizado'
    )

    worked = models.FloatField(
        'Horas Trabalhadas'
    )

    seconds_worked = models.IntegerField(
        editable=False,
        blank=True,
        null=True
    )

    # Audit fields
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Atendimento'
        verbose_name_plural = 'Atendimentos'

    def __unicode__(self):
        return '%s - %10.2f' % (self.incident.title, self.worked)