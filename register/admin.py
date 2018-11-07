from django.contrib import admin
from .models import cliente, telefone_cliente, endereco, clienteCobranca, plano, clientePlano

# Register your models here.
admin.site.register(cliente)
admin.site.register(telefone_cliente)
admin.site.register(endereco)
admin.site.register(clienteCobranca)
admin.site.register(plano)
admin.site.register(clientePlano)