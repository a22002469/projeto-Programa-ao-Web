from django.forms import ModelForm
from django import forms
from .models import Post
from .models import Quizz
from .models import Projetos
from .models import Cadeiras
from .models import Tfc


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
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira Nome'}),
        }

        labels = {

            'nome': 'Nome',

            'pergunta1': 'pergunta 1?',

            'pergunta2': 'pergunta 2?',

            'pergunta3': 'pergunta 3?',

            'pergunta4': 'pergunta 4?',



        }

        help_texts = {
        }


class ProjetosForm(ModelForm):
    class Meta:
        model = Projetos
        fields = '__all__'

        # ferramentas
        widgets = {

        }

        help_texts = {

        }

        labels = {

            'nome': 'Insira o nome',
            'descricao': 'Insira a sua descricao',
            'data' : 'Data',
            'linguagues' : 'Linguagem usada',
            'imagem':'Insira a sua imagem',

        }

        class CadeirasForm(ModelForm):
            class Meta:
                model = Cadeiras
                fields = '__all__'

                # ferramentas
                widgets = {

                }

                help_texts = {

                }

                labels = {

                    'nome': 'Insira o nome',
                    'ano': 'Ano',
                    'semestre': 'Semestre',
                    'ects': 'ects',

                }


class TfcForm(ModelForm):
    class Meta:
        model = Tfc
        fields = '__all__'

        # ferramentas
        widgets = {

        }

        help_texts = {

        }

        labels = {

            'Autores': 'Insira os autores',
            'orientadores': 'orientadores',
            'ano' : 'Data',
            'titulo' : 'titulo',
            'resumo' : 'resumo',
            'imagem':'Insira a sua imagem',
            'relatorio':'relatorio',

        }