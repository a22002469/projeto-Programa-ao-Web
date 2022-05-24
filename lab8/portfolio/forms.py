from django.forms import ModelForm
from django import forms
from .models import Post
from .models import Quizz


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

        # ferramentas
        widgets = {
            'titulo': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Introduz o teu titulo'}),

            'prioridade': forms.NumberInput(attrs={
            'class': 'form-control' ,
            'max': 3,
            'min': 1}),
        }

        help_texts = {
            'prioridade': 'Prioridade: baixa=1, media=2, alta=3'
        }

        labels = {

            'titulo': 'Título',
            'concluido': 'Concluído',
        }


class QuizzForm(ModelForm):
    class Meta:
        model = Quizz
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira o nome a apresentar'}),
        }

        labels = {

            'nome': 'Insira o nome a apresentar',

            'pergunta1': 'pergunta 1?',

            'pergunta2': 'pergunta 2?',

            'pergunta3': 'pergunta 3?',

            'pergunta4': 'pergunta 4?',



        }

        help_texts = {
        }
