from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from portfolio.forms import PostForm
from portfolio.models import Post


def home_page_view(request):
    return render(request, 'portfolio/layout.html')


# Create your views here.
def apresentacao_page_view(request):
    return render(request, 'portfolio/apresentação.html')


def licenciatura_page_view(request):
    return render(request, 'portfolio/licenciatura.html')


def formacao_page_view(request):
    return render(request, 'portfolio/formação.html')


def projetos_page_view(request):
    return render(request, 'portfolio/projetos.html')


def competencias_page_view(request):
    return render(request, 'portfolio/competencias.html')

def contacto_page_view(request):
    return render(request, 'portfolio/contacto.html')

def web_page_view(request):
    return render(request, 'portfolio/web.html')

def blog_page_view(request):
    context = {'post': Post.objects.all()}

    return render(request, 'portfolio/blog.html', context)


def view_novo_post(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form}
    return render(request, 'portfolio/nova.html', context)


def view_editar_post(request, post_id):
    post = Post.objects.get(id=post_id)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form, 'post_id': post_id}
    return render(request, 'portfolio/edita.html', context)


def view_apagar_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect(reverse('portfolio:blog'))
