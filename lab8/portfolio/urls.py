from django.urls import path
from . import views

app_name = 'portfolio'
name = 'home'
urlpatterns = [
    path('home', views.home_page_view, name='home'),
    path('', views.home_page_view),
    path('apresentação', views.apresentacao_page_view, name='apresentação'),
    path('formação', views.formacao_page_view, name='formação'),
    path('projetos', views.projetos_page_view, name='projetos'),
    path('competencias', views.competencias_page_view, name='competencias'),
]
