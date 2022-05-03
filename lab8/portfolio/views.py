from django.shortcuts import render


def home_page_view(request):
    return render(request, 'portfolio/layout.html')

# Create your views here.
