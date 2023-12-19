from django.contrib import admin
from .models import Cargo, Servico, Funcionario, Feature, Icone


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado')
    list_editable = ['ativo']


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo', 'modificado')


@admin.register(Icone)
class IconeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tag', 'ativo', 'modificado')
