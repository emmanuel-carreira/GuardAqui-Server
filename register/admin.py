from django.contrib import admin
from .models import cliente, telefone_cliente, endereco, clienteCobranca, plano, clientePlano, enderecoCobranca, hub, guardaVolume, log, usa

# Register your models here.
admin.site.register(cliente)
admin.site.register(telefone_cliente)
admin.site.register(endereco)
admin.site.register(clienteCobranca)
admin.site.register(plano)
admin.site.register(clientePlano)
admin.site.register(enderecoCobranca)
admin.site.register(hub)
admin.site.register(guardaVolume)
admin.site.register(log)
admin.site.register(usa)