#-*- coding: utf-8 -*-

from django.contrib import admin
from models import Company, Employee, Incident, Treatment


class TreatmentInline(admin.StackedInline):
    model = Treatment
    extra = 1


class EmployeeAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'email',
        'phone',
        'mobile_phone',
        'active'
    )

    fieldsets = [
        ('Dados Pessoais', {
            'fields': [
                'name',
                'email',
                'phone',
                'mobile_phone',
                'admission_date'
            ]
        }),
        ('Endereço', {
            'fields': [
                'street',
                'number',
                'complement',
                'neighborhood'
            ]
        }),
        ('Redes Sociais', {
            'fields': [
                'facebook',
                'twitter',
                'linkedin'
            ]
        }),
        (None, {
            'fields': [
                'active'
            ]
        })
    ]


class CompanyAdmin(admin.ModelAdmin):

    filter_horizontal = ('users',)

    list_display = (
        'fancy_name',
        'cnpj',
        'email',
        'phone',
        'active'
    )

    fieldsets = [
        ('Dados Empresa', {
            'fields': [
                'logo',
                'name',
                'fancy_name',
                'cnpj',
                'email',
                'phone',
            ]
        }),
        ('Endereço', {
            'fields': [
                'street',
                'number',
                'complement',
                'neighborhood',
                'city',
            ]
        }),
        ('Redes Sociais', {
            'fields': [
                'facebook',
                'twitter',
                'linkedin'
            ]
        }),
        ('Contatos', {
            'fields': {
                'users'
            }
        }),
        (None, {
            'fields': [
                'active'
            ]
        })
    ]


class IncidentAdmin(admin.ModelAdmin):

    list_filter = ['company', 'responsible']

    inlines = [TreatmentInline]

    list_display = (
        'date_open',
        'title',
        'requestor',
        'company',
        'responsible',
        'progress'
    )


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Incident, IncidentAdmin)
