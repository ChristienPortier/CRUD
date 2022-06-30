from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(blank=True, null=True)
    pontuacao = models.IntegerField(blank=True, null=True)
    habilitado = models.BooleanField(blank=True, null=True)
    observacao =  models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

     