from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from portfolio.forms import PostForm
from portfolio.models import Post
from portfolio.forms import QuizzForm
from portfolio.models import Quizz
from portfolio.models import Projetos
from portfolio.models import Cadeiras
from portfolio.models import Sobre
from portfolio.models import Web
from portfolio.models import Tfc

from portfolio.quizz import desenha_graficodados


def home_page_view(request):
    return render(request, 'portfolio/home.html')


# Create your views here.
def apresentacao_page_view(request):
    return render(request, 'portfolio/apresentação.html')


def licenciatura_page_view(request):
    context = {'cadeiras': Cadeiras.objects.all()}
    return render(request, 'portfolio/licenciatura.html', context)


def sobre_page_view(request):
    context = {'sobre': Sobre.objects.all()}
    return render(request, 'portfolio/sobre.html', context)


def projetos_page_view(request):
    context = {'projetos': Projetos.objects.all()}
    return render(request, 'portfolio/projetos.html', context)


def login_page_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            context = {'post': Post.objects.all()}
            return render(request, 'portfolio/blog.html', context)
        else:
            return render(request, 'portfolio/login.html', {'message': "Credenciais inválidos"})

    return render(request, 'portfolio/login.html')


def logout_page_view(request):
    logout(request)
    return render(request, 'portfolio/home.html')


def competencias_page_view(request):
    return render(request, 'portfolio/competencias.html')

def tfc_page_view(request):
    context = {'tfc' : Tfc.objects.all()}
    return render(request, 'portfolio/tfc.html', context)


def contacto_page_view(request):
    return render(request, 'portfolio/contacto.html')


def quizz_page_view(request):
    desenha_graficodados(Quizz.objects.all())
    form = QuizzForm(request.POST, use_required_attribute=False)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(request.path_info)

    context = {
        'form': form,
    }

    return render(request, 'portfolio/quizz.html', context)


def web_page_view(request):
    context = {'web': Web.objects.all()}
    return render(request, 'portfolio/web.html', context)


def blog_page_view(request):
    context = {'post': Post.objects.all()}

    return render(request, 'portfolio/blog.html', context)


@login_required
def view_novo_post(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form}
    return render(request, 'portfolio/nova.html', context)


@login_required
def view_editar_post(request, post_id):
    post = Post.objects.get(id=post_id)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form, 'post_id': post_id}
    return render(request, 'portfolio/edita.html', context)


@login_required
def view_apagar_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect(reverse('portfolio:blog'))

def api_page_view(request):

    return render(request, 'portfolio/api.html')
