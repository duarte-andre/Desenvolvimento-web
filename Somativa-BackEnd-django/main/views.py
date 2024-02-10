from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from datetime import timedelta, datetime
from django.db.models.signals import post_save, post_delete
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.db.models import Avg
from django.db.models import F
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly
from datetime import datetime
from .customFilters import *


def strToDate(strDate):
    return datetime.strptime(strDate, '%y-%m-%d').date()


#creating custom model viewset allowing multiple registers
class CustomModelViewSet(ModelViewSet):
    def create(self, request, *args, **kwargs):
       Myserializer =  self.get_serializer(data=request.data, many=isinstance(request.data, list))
       Myserializer.is_valid(raise_exception=True)
       self.perform_create(Myserializer)
       headers = self.get_success_headers(Myserializer.data)
       return Response(Myserializer.data, status=201, headers=headers)


# Create your views here.

class ClienteView(ModelViewSet):
    queryset = Cliente.objects.all() 
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = ClienteFilter
    ordering_fields = '__all__'
       

class FuncionarioView(ModelViewSet):
    queryset = Funcionario.objects.all() 
    serializer_class = FuncionarioSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = FuncionarioFilter
    ordering_fields = '__all__'

class CategoriaServicoView(ModelViewSet):
    queryset = CategoriaServico.objects.all() 
    serializer_class = CategoriaServicoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = CategoriaServicoFilter
    ordering_fields = '__all__'

class ProdutoView(ModelViewSet):
    queryset = Produto.objects.all() 
    serializer_class = ProdutoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = ProdutoFilter
    ordering_fields = '__all__'
    

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(quantidade_em_estoque__lt=4)

       
        if queryset.exists():
            # Gere um aviso ou notificação, por exemplo, uma resposta de API
            mensagem = "Alguns produtos têm quantidade em estoque menor que 4."
            return Response({"mensagem": mensagem}, status=status.HTTP_400_BAD_REQUEST)

        return queryset

class AutomovelView(ModelViewSet):
    queryset = Automovel.objects.all() 
    serializer_class = AutomovelSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = AutomovelFilter
    ordering_fields = '__all__'

class ManutencaoView(CustomModelViewSet):
    queryset = Manutencao.objects.all() 
    serializer_class = ManutencaoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = ManutencaoFilter
    ordering_fields = '__all__'

class ItemManutencaoView(ModelViewSet):
    queryset = ItemManutencao.objects.all() 
    serializer_class = ItemManutencaoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = ItemManutencaoFilter
    ordering_fields = '__all__'

    def create(self, request, *args, **kwargs):
        # Chama o método create da classe base
        response = super().create(request, *args, **kwargs)
        
        # Atualiza a quantidade em estoque do produto
        item_manutencao = self.get_object()
        produto = item_manutencao.produto
        quantidade_usada = item_manutencao.quantidade_usada
        
        if quantidade_usada > 0:
            produto.quantidade_em_estoque -= quantidade_usada
            produto.save()
        
        return response

class PagamentoView(ModelViewSet):
    queryset = Pagamento.objects.all() 
    serializer_class = PagamentoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = PagamentoFilter
    ordering_fields = '__all__'

    def create(self, request, *args, **kwargs):
        dados = request.data
        pagamentoSerialized = PagamentoSerializer(data=dados, many=False)
        pagamentoSerialized.is_valid(raise_exception=True)
        pagamentoSerialized.save()
        return Response(pagamentoSerialized.data)

#data_reserva
#endDate
class ReservaView(CustomModelViewSet):
    queryset = Reserva.objects.all() 
    serializer_class = ReservaSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = ReservaFilter
    ordering_fields = '__all__'

@receiver(post_save, sender=Reserva)
def update_disponibilidade_on_create(sender, instance, created, **kwargs):
    if created:
        # Atualize a disponibilidade para a data e posto de trabalho apropriados
        disponibilidade, created = DisponibilidadeReserva.objects.get_or_create(data_reserva=instance.data_reserva)
        setattr(disponibilidade, f"posto_{instance.posto_trabalho}_reservas", F('posto_{instance.posto_trabalho}_reservas') + 1)
        disponibilidade.save()

@receiver(post_delete, sender=Reserva)
def update_disponibilidade_on_delete(sender, instance, **kwargs):
    disponibilidade = DisponibilidadeReserva.objects.get(data_reserva=instance.data_reserva)
    setattr(disponibilidade, f"posto_{instance.posto_trabalho}_reservas", F('posto_{instance.posto_trabalho}_reservas') - 1)
    disponibilidade.save()


class DisponibilidadeReservaView(CustomModelViewSet):
    queryset = DisponibilidadeReserva.objects.all() 
    serializer_class = DisponibilidadeReservaSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = DisponibilidadeReservaFilter
    ordering_fields = '__all__'