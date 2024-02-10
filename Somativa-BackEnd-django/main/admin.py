from django.contrib import admin
from .models import *
# Register your models here.

class adminCliente(admin.ModelAdmin):
    list_display = ('id', 'nome', 'endereco','numero_telefone','email')
    list_display_links = ('id', 'nome','numero_telefone','email',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Cliente,adminCliente)

class adminFuncionario(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cargo')
    list_display_links = ('id','nome',)
    search_fields = ('nome',)
    list_per_page = 5

admin.site.register(Funcionario,adminFuncionario)

class adminCategoriaServico(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(CategoriaServico,adminCategoriaServico)

class adminProduto(admin.ModelAdmin):
    list_display = ('id','nome','quantidade_em_estoque','codigo_fabricante','nome_fabricante','valor_compra','valor_venda')
    list_display_links = ('id', 'nome',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Produto,adminProduto)

class adminAutomovel(admin.ModelAdmin):
    list_display = ('id','marca', 'modelo', 'ano', 'categoria')
    list_display_links = ('id','marca', 'modelo','categoria')
    search_fields = ('categoria', 'marca', 'modelo', )
    list_per_page = 10

admin.site.register(Automovel,adminAutomovel)

class AdminManutencao(admin.ModelAdmin):
    list_display = ('id','cliente', 'automovel', 'data_e_hora', 'valor_total','status', 'desconto', 'funcionario_responsavel' )
    list_display_links = ('id', 'cliente', 'automovel', 'data_e_hora','status',)  # Adicione outros campos de filtro conforme necessário
    search_fields = ('cliente__nome', 'automovel__marca', 'automovel__modelo')  # Você pode procurar por campos relacionados
    list_per_page = 10

admin.site.register(Manutencao, AdminManutencao)

class adminItemManutencao(admin.ModelAdmin):
    list_display = ('id','manutencao', 'categoria_servico', 'produto', 'quantidade_usada')
    list_display_links = ('id', 'manutencao',)
    search_fields = ('manutencao__cliente__nome', 'categoria_servico__nome', 'produto__nome',)
    list_per_page = 10

admin.site.register(ItemManutencao, adminItemManutencao)

class adminPagamento(admin.ModelAdmin):
    list_display = ('id','manutencao', 'categoria_pagamento', 'descricao', 'valor_final')
    list_display_links = ('id','categoria_pagamento',)
    search_fields = ('manutencao__cliente__nome','categoria_pagamento','descricao',)
    list_per_page = 10

admin.site.register(Pagamento, adminPagamento)

class adminReserva(admin.ModelAdmin):
    list_display = ('id','cliente', 'data_reserva', 'posto_trabalho')
    list_display_links = ('id', )
    search_fields = ('cliente__nome','posto_trabalho',)
    list_per_page = 10

admin.site.register(Reserva, adminReserva)
    

class adminDisponibilidadeReserva(admin.ModelAdmin):
    list_display = ('data', 'posto_1_reservas', 'posto_2_reservas', 'posto_3_reservas')
    search_fields = ('data',)
    list_per_page = 10

admin.site.register(DisponibilidadeReserva, adminDisponibilidadeReserva)

