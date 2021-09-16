from django.contrib import admin
from contatos.models import Contato

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email', 'data_criacao', 'categoria')
    list_display_links = ('id', 'nome')
    list_filter = ('categoria',)

admin.site.register(Contato, ContatoAdmin)

