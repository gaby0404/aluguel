from django.db import models

class Imovel(models.Model):
    titulo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    valor_aluguel = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)
    logradouro = models.CharField(max_length=200)
    cep = models.CharField(max_length=12)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return self.titulo