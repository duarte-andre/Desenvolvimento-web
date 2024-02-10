from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *

router = DefaultRouter()
router.register(r'cliente',ClienteView)
router.register(r'Funcionario',FuncionarioView)
router.register(r'CategoriaServico',CategoriaServicoView)
router.register(r'Produto',ProdutoView)
router.register(r'Automovel',AutomovelView)
router.register(r'Manutencao',ManutencaoView)
router.register(r'ItemManutencao',ItemManutencaoView)
router.register(r'Pagamento',PagamentoView)
router.register(r'Reserva',ReservaView)
router.register(r'DisponibilidadeReserva',DisponibilidadeReservaView)

urlpatterns = router.urls