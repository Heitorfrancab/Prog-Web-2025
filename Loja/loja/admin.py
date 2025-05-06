from django.contrib import admin
# Register your models here.
from .models import * #imporata nossos models
class FabricanteAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'
class ProdutoAdmin(admin.ModelAdmin):
    search_fields = ('Produto',)
    date_hierarchy = 'criado_em'
    list_display = ('Produto', 'destaque', 'promocao', 'msgPromocao', 'preco', 'categoria',)
    empty_value_display = 'Vazio'
admin.site.register(Fabricante, FabricanteAdmin) #adiciona a interface do adm
admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)