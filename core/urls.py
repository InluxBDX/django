from django.conf.urls import url, include 
from .views import (home, 
lista_pessoas, 
lista_veiculos,
lista_movrotativos,
lista_mensalistas,
lista_mov_mensalistas,
pessoa_novo,
veiculo_novo,
mov_rotativo_novo,
novo_mensalista,
mov_mensalista_novo,
pessoa_update,
veiculo_update,
movrotativo_update,
mensalista_update,
mov_mensalista_update,
pessoa_delete,
veiculo_delete,
movorativo_delete,
mensalista_delete,
mov_mensalista_delete,
)


urlpatterns = [
url(r'^$', home, name='core_home'),

url(r'^pessoas/', lista_pessoas, name='core_lista_pessoas'),
url(r'^pessoa-novo/', pessoa_novo, name='core_pessoa_novo'),
url(r'^pessoa-update/(?P<id>\d+)/', pessoa_update, name='core_pessoa_update'),
url(r'^pessoa-delete/(?P<id>\d+)/', pessoa_delete, name='core_pessoa_delete'),


url(r'^veiculos/', lista_veiculos, name='core_lista_veiculos'),
url(r'^veiculo-novo/', veiculo_novo, name='core_veiculo_novo'),
url(r'^veiculo-update/(?P<id>\d+)/', veiculo_update, name='core_veiculo_update'),
url(r'^veiculo-delete/(?P<id>\d+)/', veiculo_delete, name='core_veiculo_delete'),

url(r'^mov-rot-list/', lista_movrotativos, name='core_lista_movrotativos'),
url(r'^mov-rot-novo/', mov_rotativo_novo, name='core_mov_rotativonovo'),
url(r'^mov-rot-update/(?P<id>\d+)/', movrotativo_update, name='core_movrot_update'),
url(r'^mov-rot-delete/(?P<id>\d+)/', movorativo_delete, name='core_movrot_delete'),

url(r'^mensalista/', lista_mensalistas, name='core_lista_mensalistas'),
url(r'^mensalista-novo/', novo_mensalista, name='core_mensalista_novo'),
url(r'^mensalista-update/(?P<id>\d+)/', mensalista_update, name='core_mensalista_update'),
url(r'^mensalista-delete/(?P<id>\d+)/', mensalista_delete, name='core_mensalista_delete'),

url(r'^mov-mensalista/', lista_mov_mensalistas, name='core_lista_mov-mensalistas'),
url(r'^mov-mensalista-novo/', mov_mensalista_novo, name='core_movmensalistas_novo'),
url(r'^mov-mensalista-update/(?P<id>\d+)/', mov_mensalista_update, name='core_mov_mensalista_update'),
url(r'^mov-mensalista-delete/(?P<id>\d+)/', mov_mensalista_delete, name='core_mov_mensalista_delete'),]