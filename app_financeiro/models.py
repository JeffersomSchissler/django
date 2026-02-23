from django.db import models
from django.db.models import PROTECT


class Categorias(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)

class Movimentacao(models.Model):

    class Tipo(models.TextChoices):
        RECEITAS = 'R', 'Receitas'
        DESPESAS = 'D', 'Despesas'

    tipo = models.CharField(max_length=1, choices=Tipo.choices)

    descricao = models.CharField(max_length=50)
    data = models.DateField()
    categorias = models.ForeignKey(Categorias, on_delete=PROTECT)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.descricao}"

