from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import (
	Pessoa, 
	Veiculo, 
	MovRotativo, 
	Mensalista, 
	MovMensalista,
)
from .forms import (
	PessoaForm, 
	VeiculoForm, 
	MovRotativoForm, 
	MensalistaForm,
	MovMensalistaForm
)

# Create your views here.

def home(request):
	context = {'mensagem': 'ola inferno'}
	return render(request, 'core/index.html', context)

def lista_pessoas(request):
	pessoas = Pessoa.objects.all()
	form = PessoaForm()
	data = {'pessoas': pessoas, 'form' : form}
	return render(request,'core/lista_pessoas.html', data)


def pessoa_novo(request):
	form = PessoaForm(request.POST or None)
	if form.is_valid():
		form.save()
	return redirect('core_lista_pessoas')


def pessoa_update(request,id):
	data = {}
	pessoa = Pessoa.objects.get(id=id)
	form = PessoaForm(request.POST or None, instance=pessoa)
	data['pessoa'] = pessoa
	data['form'] = form

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('core_lista_pessoas')
	else:
		return render(request, 'core/update_pessoa.html', data)

def pessoa_delete(request,id):
	pessoa = Pessoa.objects.get(id=id)
	if request.method == 'POST':
		pessoa.delete()
		return redirect('core_lista_pessoas')
	else:
		return render(request, 'core/delete_confirm.html', {'obj': pessoa})


def lista_veiculos(request):
	veiculos = Veiculo.objects.all()
	form = VeiculoForm()
	data = {'veiculos': veiculos, 'form' : form}
	return render(request,'core/lista_veiculos.html',data)


def veiculo_novo(request):
	form = VeiculoForm(request.POST or None)
	if form.is_valid():
		form.save()
	return redirect('core_lista_veiculos')

def veiculo_update(request,id):
	data = {}
	veiculo = Veiculo.objects.get(id=id)
	form = VeiculoForm(request.POST or None, instance=veiculo)
	data['veiculo'] = veiculo
	data['form'] = form

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('core_lista_veiculos')
	else:
		return render(request, 'core/update_veiculo.html', data)

def veiculo_delete(request,id):
	veiculo = Veiculo.objects.get(id=id)
	if request.method == 'POST':
		veiculo.delete()
		return redirect('core_lista_veiculos')
	else:
		return render(request, 'core/delete_confirm.html', {'obj': veiculo})

def lista_movrotativos(request):
	movrot = MovRotativo.objects.all()
	form = MovRotativoForm()
	data = {'movrot': movrot, 'form': form}
	return render(request,'core/lista_movrotativos.html', data)


def mov_rotativo_novo(request):
	form = MovRotativoForm(request.POST or None)
	if form.is_valid():
		form.save()
	return redirect('core_lista_movrotativos')


def movrotativo_update(request,id):
	data = {}
	mov_rotativo = MovRotativo.objects.get(id=id)
	form = MovRotativoForm(request.POST or None, instance=mov_rotativo)
	data['mov_rotativo'] = mov_rotativo
	data['form'] = form

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('core_lista_movrotativos')
	else:
		return render(request, 'core/update_movrot.html', data)



def movorativo_delete(request,id):
	movroativo = MovRotativo.objects.get(id=id)
	if request.method == 'POST':
		movroativo.delete()
		return redirect('core_lista_movrotativos')
	else:
		return render(request, 'core/delete_confirm.html', {'obj': movroativo})

def lista_mensalistas(request):
	mensalista = Mensalista.objects.all()
	form = MensalistaForm()
	data = {'mensalistas': mensalista, 'form': form}
	return render(request,'core/lista_mensalistas.html', data)

def novo_mensalista(request):
	form = MensalistaForm(request.POST or None)
	if form.is_valid():
			form.save()
	return redirect('core_lista_mensalistas')

def mensalista_update(request,id):
	data = {}
	mensalista = Mensalista.objects.get(id=id)
	form = MensalistaForm(request.POST or None, instance=mensalista)
	data['mensalista'] = mensalista
	data['form'] = form

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('core_lista_mensalistas')
	else:
		return render(request, 'core/update_mensalista.html', data)


def mensalista_delete(request,id):
	mensalista = Mensalista.objects.get(id=id)
	if request.method == 'POST':
		mensalista.delete()
		return redirect('core_lista_mensalistas')
	else:
		return render(request, 'core/delete_confirm.html', {'obj': mensalista})		

def lista_mov_mensalistas(request):
	mov_mensalistas = MovMensalista.objects.all()
	form = MovMensalistaForm()
	data = {'mov_mensalistas': mov_mensalistas, 'form': form}
	return render(request,'core/lista_mov_mensalistas.html', data)

def mov_mensalista_novo(request):
	form = MovMensalistaForm(request.POST or None)
	if form.is_valid():
		form.save()
	return redirect('core_lista_mov-mensalistas')


def mov_mensalista_update(request,id):
	data = {}
	movmensalista = MovMensalista.objects.get(id=id)
	form = MovMensalistaForm(request.POST or None, instance=movmensalista)
	data['movmensalista'] = movmensalista
	data['form'] = form

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('core_lista_mov-mensalistas')
	else:
		return render(request, 'core/update_movmensalista.html', data)


def mov_mensalista_delete(request,id):
	mov_mensalista = MovMensalista.objects.get(id=id)
	if request.method == 'POST':
		mov_mensalista.delete()
		return redirect('core_lista_mov-mensalistas')
	else:
		return render(request, 'core/delete_confirm.html', {'obj': mov_mensalista})		