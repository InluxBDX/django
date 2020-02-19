from django.db import models
import math


# Create your models here.


class Pessoa(models.Model):
	nome = models.CharField(max_length=100)
	endereco = models.CharField(max_length=200)
	telefone = models.CharField(max_length=20)

	def __str__(self):
		return self.nome + " " + self.endereco + " " + self.telefone
	  
class Marca(models.Model):
	nome = models.CharField(max_length=50)

	def __str__(self):
		return self.nome


class Veiculo(models.Model):
	marca = models.ForeignKey('Marca', on_delete=models.PROTECT)
	proprietario = models.ForeignKey('Pessoa', on_delete=models.PROTECT)
	placa = models.CharField(max_length=7)
	cor = models.CharField(max_length=15)
	observacoes = models.TextField()
	

	def __str__(self):
		return self.marca.nome + " " + self.placa + " " + self.cor + " " + self.proprietario.nome

class Parametros(models.Model):
	valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
	valor_mes = models.DecimalField(max_digits=6, decimal_places=2)

	def __str__(self):
		return "Parâmetros Gerais Sistema"

class MovRotativo(models.Model):

	Pago = 'PG'
	Pendente = 'PE'

	SITUACAO = [(Pago, 'Pago'), (Pendente, 'Pendente'),]

	data_entrada = models.DateTimeField(auto_now=False)
	data_saida = models.DateTimeField(auto_now=False, null=True, blank=True)
	valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
	veiculo = models.ForeignKey('Veiculo', on_delete=models.PROTECT)
	situacao = models.CharField(
		max_length=2,
		choices = SITUACAO,
		default=Pendente
	)

	def __str__(self):
		return self.veiculo.placa

	def horas_total(self):
		try:
			return math.ceil((self.data_saida - self.data_entrada).total_seconds() / 3600)
		except:
			pass

	def total(self):
		try:
			return self.valor_hora * self.horas_total()
		except:
			pass

class Mensalista(models.Model):
	veiculo = models.ForeignKey('Veiculo', on_delete=models.PROTECT)
	inicio = models.DateField()
	valor_mes = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return str(self.veiculo) + '-' + str(self.inicio)

class MovMensalista(models.Model):
	mensalista = models.ForeignKey('Mensalista', on_delete=models.PROTECT)
	data_pagamento = models.DateField()
	total_pagamento = models.DecimalField(max_digits=6, decimal_places=2)


	def __str__(self):
		return str(self.mensalista) + ' - ' + str(self.total_pagamento)