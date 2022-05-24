from django.db import models


class Post(models.Model):
    autor = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.titulo}"


class Quizz(models.Model):
    nome = models.CharField(max_length=50)
    pergunta1 = models.CharField(max_length=50)
    pergunta2 = models.CharField(max_length=50)
    pergunta3 = models.CharField(max_length=50)
    pergunta4 = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome}"
