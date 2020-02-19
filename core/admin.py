from django.contrib import admin
from .models import (
	Marca, 
	Veiculo, 
	Pessoa, 
	Parametros, 
	MovRotativo,
	Mensalista,
	MovMensalista
)

class MovRotativoAdmin(admin.ModelAdmin):
	list_display = (
		'data_entrada', 'data_saida', 'valor_hora', 'veiculo', 'situacao', 'total',
		 'horas_total', 'veiculo')

	def veiculo(self,obj):
		return obj.veiculo

class MensalistaAdmin(admin.ModelAdmin):
	list_display = ('veiculo', 'inicio', 'valor_mes')

class MovMensalistaAdmin(admin.ModelAdmin):
	list_display = ('mensalista', 'data_pagamento', 'total_pagamento')

admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
admin.site.register(Parametros)
admin.site.register(MovRotativo, MovRotativoAdmin)
admin.site.register(Mensalista, MensalistaAdmin)
admin.site.register(MovMensalista, MovMensalistaAdmin)



# Register your models here.
