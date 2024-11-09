from django.db import models
from datetime import date

# Create your models here.

class Categoria(models.Model):

    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome

class Livros(models.Model):

    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    co_autor = models.CharField(max_length=50, blank=True)
    data_cadastro = models.DateField(default=date.today)
    emprestado = models.BooleanField(default=False)
    nome_emprestado = models.CharField(max_length=50, blank=True)
    data_emprestimo = models.DateTimeField(blank=True, null=True)
    data_devolucao = models.DateTimeField(blank=True, null=True)
    tempo_duracao = models.DateField(blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    class Meta:

        verbose_name = 'Livro'
    
    def __str__(self):

        return self.nome
