from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Cliente(models.Model):
    user = models.OneToOneField(User, related_name="userCliente", on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    numero_telefone = models.CharField(max_length=20)
    email = models.EmailField()
    
    def __str__(self):
        return self.endereco
    
@receiver (post_save, sender=User)
def create_user_custom(sender, instance, created, **kwargs):
    if created:
        Cliente.objects.create(nome=instance)

@receiver (post_save, sender=User)
def save_user_custom(sender, instance, created, **kwargs):
    instance.customuser.save()      

class Funcionario(models.Model):
    user = models.OneToOneField(User, related_name="userFuncionario", on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome.cargo
    
@receiver (post_save, sender=User)
def create_user_custom(sender, instance, created, **kwargs):
    if created:
        Funcionario.objects.create(nome=instance)

@receiver (post_save, sender=User)
def save_user_custom(sender, instance, created, **kwargs):
    instance.customuser.save()

class CategoriaServico(models.Model):
    nome = models.CharField(max_length=255)
    valor_mao_de_obra = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.nome.valor

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    quantidade_em_estoque = models.IntegerField()
    codigo_fabricante = models.CharField(max_length=255)
    nome_fabricante = models.CharField(max_length=255)
    valor_compra = models.DecimalField(max_digits=10, decimal_places=2)
    valor_venda = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.nome.quantidade_em_estoque.codigo_fabricante.nome_fabricante.valor_compra.valor_venda

class Automovel(models.Model):
    CATEGORIAS = (
        ('Carro', 'Carro'),
        ('Moto', 'Moto'),
        
    )
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    marca = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    ano = models.IntegerField()

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano})"
    

class Manutencao(models.Model):
    STATUS_CHOICES = (
        ('Pendente', 'Pendente'),
        ('Aprovado', 'Aprovado'),
        ('Cancelado', 'Cancelado'),
    )
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    automovel = models.ForeignKey(Automovel, on_delete=models.CASCADE)
    data_e_hora = models.DateTimeField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    desconto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    funcionario_responsavel = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Manutenção de {self.automovel} em {self.data_e_hora}"

class ItemManutencao(models.Model):
    manutencao = models.ForeignKey(Manutencao, on_delete=models.CASCADE)
    categoria_servico = models.ForeignKey(CategoriaServico, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade_usada = models.PositiveIntegerField()
    
    def __str__(self):
        return f"Item de Manutenção: {self.categoria_servico} ({self.produto})"

class Pagamento(models.Model):
    manutencao = models.ForeignKey(Manutencao, on_delete=models.CASCADE)
    CATEGORIAS_PAGAMENTO = (
        ('Pix', 'Pix'),
        ('Boleto', 'Boleto'),
        ('Cartão de Crédito', 'Cartão de Crédito'),
    )
    categoria_pagamento = models.CharField(max_length=20, choices=CATEGORIAS_PAGAMENTO)
    descricao = models.CharField(max_length=255)
    valor_final = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Pagamento para Manutenção de {self.manutencao.automovel}"
    
class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_reserva = models.DateField()
    posto_trabalho = models.IntegerField(choices=[(1, 'Posto 1'), (2, 'Posto 2'), (3, 'Posto 3')])
    
    def __str__(self):
        return f"Reserva de {self.cliente} para o dia {self.data_reserva}"
    
class DisponibilidadeReserva(models.Model):
    data = models.DateField()
    posto_1_reservas = models.PositiveIntegerField(default=0)
    posto_2_reservas = models.PositiveIntegerField(default=0)
    posto_3_reservas = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"Disponibilidade para Reserva no(s) posto(s) {self.data}"
    

