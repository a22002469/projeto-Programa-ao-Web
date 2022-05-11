from django.db import models


class Post(models.Model):
    autor = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=500)
