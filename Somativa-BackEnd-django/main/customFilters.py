from rest_framework import filters
import django_filters
from .models import *


class ClienteFilter (django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')
    endereco = django_filters.CharFilter(lookup_expr='icontains')
    numero_telefone = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Cliente
        fields = ['nome', 'endereco', 'numero_telefone', 'email']


class ProdutoFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')
    quantidade_em_estoque = django_filters.CharFilter(lookup_expr='icontains')
    codigo_fabricante = django_filters.CharFilter(lookup_expr='icontains')
    nome_fabricante = django_filters.CharFilter(lookup_expr='icontains')
    nome = django_filters.CharFilter(lookup_expr='icontains')
    nome = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Produto
        fields = ['nome', 'quantidade_em_estoque', 'codigo_fabricante', 'nome_fabricante']


class FuncionarioFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')
    cargo = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Funcionario
        fields = ['nome', 'cargo']


class CategoriaServicoFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')
    valor_mao_de_obra = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = CategoriaServico
        fields = ['nome', 'valor_mao_de_obra']

class AutomovelFilter(django_filters.FilterSet):
    marca = django_filters.CharFilter(lookup_expr='icontains')
    modelo = django_filters.CharFilter(lookup_expr='icontains')
    ano = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Automovel
        fields = ['marca', 'modelo', 'ano']

class ManutencaoFilter(django_filters.FilterSet):
    cliente = django_filters.CharFilter(lookup_expr='icontains')
    valor_total = django_filters.CharFilter(lookup_expr='icontains')
    status = django_filters.CharFilter(lookup_expr='icontains')
    funcionario_responsavel = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Manutencao
        fields = ['cliente', 'valor_total', 'status', 'funcionario_responsavel']

class ItemManutencaoFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')
    quantidade_em_estoque = django_filters.CharFilter(lookup_expr='icontains')
    codigo_fabricante = django_filters.CharFilter(lookup_expr='icontains')
    nome_fabricante = django_filters.CharFilter(lookup_expr='icontains')
    valor_compra = django_filters.CharFilter(lookup_expr='icontains')
    valor_venda = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Produto
        fields = ['nome', 'quantidade_em_estoque', 'codigo_fabricante', 'nome_fabricante', 'valor_compra', 'valor_venda']


class PagamentoFilter(django_filters.FilterSet):
    categoria_pagamento = django_filters.CharFilter(lookup_expr='icontains')
    descricao = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Pagamento
        fields = ['categoria_pagamento', 'descricao']

class ReservaFilter(django_filters.FilterSet):
    cliente = django_filters.CharFilter(lookup_expr='icontains')
    data_reserva = django_filters.CharFilter(lookup_expr='icontains')
    posto_trabalho = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Reserva
        fields = ['cliente', 'data_reserva', 'posto_trabalho']

class DisponibilidadeReservaFilter(django_filters.FilterSet):
    posto_1_reservas = django_filters.CharFilter(lookup_expr='icontains')
    posto_2_reservas = django_filters.CharFilter(lookup_expr='icontains')
    posto_3_reservas = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = DisponibilidadeReserva
        fields = ['posto_1_reservas', 'posto_2_reservas', 'posto_3_reservas']
       