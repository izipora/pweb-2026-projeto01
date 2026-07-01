from django.db import models

class Sobre(models.Model):
    titulo = models.CharField(max_length=100)
    ano = models.CharField(max_length=4)
    diretor = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo
    
class Autora(models.Model):
    nome = models.CharField(max_length=100)
    funcao = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150)
    tecnologia = models.CharField(max_length=150)

    def __str__(self):
        return self.nome
    
class Elenco(models.Model):
    nome = models.CharField(max_length=50)
    dublador = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to="elenco/")

    def __str__(self):
        return self.nome