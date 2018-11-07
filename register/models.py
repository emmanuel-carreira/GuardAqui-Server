from django.db import models
from django.conf import settings


# Create your models here.

#Client model
class cliente(models.Model):

    id = models.PositiveIntegerField(primary_key=True)
    nome = models.CharField(max_length=15)
    sobrenome = models.CharField(max_length=15)
    dt_nascimento = models.DateTimeField()
    nacionalidade = models.CharField(max_length=15)

    def __str__(self):
        return str(self.id) + ' - ' + self.nome

#Telephone model
class telefone_cliente(models.Model):

    id = models.ForeignKey(cliente, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=12, primary_key=True)

    class Meta:
        verbose_name_plural = 'Telefones Clientes'

    def __str__(self):
        return str(self.id) + ' - ' + str(self.telefone)

#Andress model
class endereco(models.Model):

    idCliente = models.ForeignKey('cliente', on_delete=models.CASCADE, unique=True)
    cep = models.CharField(max_length=10)
    rua = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    complemento = models.CharField(max_length=50)
    numero = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'Endereços Clientes'

    def __str__(self):
        return str(self.idCliente)

#Credit card model
class clienteCobranca(models.Model):

    idCliente = models.ForeignKey('cliente', on_delete=models.CASCADE)
    numeroCartao = models.CharField(max_length=20, unique=True, null=False, primary_key=True)
    cvv = models.CharField(max_length=3, null=False)
    validade = models.CharField(max_length=5, null=False)
    bandeiraCartao = models.CharField(max_length=25)

    class Meta:
        verbose_name_plural = 'Cartões'

    def __str__(self):
        return str(self.idCliente) + ' - ' + str(self.bandeiraCartao)

#Signature type model
class plano(models.Model):
    idPlano = models.PositiveIntegerField(primary_key=True)
    tipo = models.CharField(max_length=30)
    valor = models.PositiveIntegerField()

    def __str__(self):
        return str(self.idPlano) + ' - ' + str(self.tipo)

#Client signature type model
class clientePlano(models.Model):
    idCliente = models.ForeignKey('cliente', on_delete=models.CASCADE)
    idPlano = models.ForeignKey('plano', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Planos dos clientes'

    def __str__(self):
        return str(self.idCliente) + ' - ' + str(self.idPlano)