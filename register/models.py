from django.db import models


# Create your models here.

#User model
class cliente(models.Model):

    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=15)
    sobrenome = models.CharField(max_length=15)
    dt_nascimento = models.DateTimeField()
    nacionalidade = models.CharField(max_length=15)

    #class Meta:
     #   verbose_name_plural = 'Clientes'

    def __str__(self):
        return str(self.id) + ' - ' + self.nome

class telefone_cliente(models.Model):

    id = models.ForeignKey(cliente, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=12, primary_key=True)

    class Meta:
        verbose_name_plural = 'Telefones Clientes'

    def __str__(self):
        return str(self.id) + ' - ' + str(self.telefone)