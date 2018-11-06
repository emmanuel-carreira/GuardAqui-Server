from django.contrib import admin
from .models import cliente, telefone_cliente

# Register your models here.
admin.site.register(cliente)
admin.site.register(telefone_cliente)