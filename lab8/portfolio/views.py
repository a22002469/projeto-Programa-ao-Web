from django.shortcuts import render


def home_page_view(request):
    return render(request, 'portfolio/layout.html')


# Create your views here.
def apresentacao_page_view(request):
    return render(request, 'portfolio/apresentação.html')

def formacao_page_view(request):
    return render(request, 'portfolio/formação.html')

def projetos_page_view(request):
    return render(request, 'portfolio/projetos.html')

def competencias_page_view(request):
    return render(request, 'portfolio/competencias.html')

def blog_page_view(request):
    return render(request, 'portfolio/blog.html')