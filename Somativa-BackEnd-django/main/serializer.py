from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        many= True

class ClienteSerializer(serializers.ModelSerializer):
    nome = UserSerializer(read_only=True)
    class Meta:
        model = Cliente
        fields = '__all__'
        many = True

class FuncionarioSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Funcionario
        fields = '__all__'
        many = True

class CategoriaServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaServico
        fields = '__all__'
        many = True
    


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
        many = True

class AutomovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Automovel
        fields = '__all__'
        many = True

class ManutencaoSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(read_only=True)
    automovel = AutomovelSerializer(read_only=True)
    funcionario_responsavel= FuncionarioSerializer(read_only=True)
    class Meta:
        model = Manutencao
        fields = '__all__'
        many = True

class ItemManutencaoSerializer(serializers.ModelSerializer):
    manutencao = ManutencaoSerializer(read_only=True)
    categoria_servico = CategoriaServicoSerializer(read_only=True)
    produto = ProdutoSerializer(read_only=True)
    class Meta:
        model = ItemManutencao
        fields = '__all__'
        many = True

class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = '__all__'
        many = True
        
class ReservaSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(read_only=True)
    class Meta:
        model = Reserva
        fields = '__all__'
        many = True

class DisponibilidadeReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisponibilidadeReserva
        fields = '__all__'
        many = True
        