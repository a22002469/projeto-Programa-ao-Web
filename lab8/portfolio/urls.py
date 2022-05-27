from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('home', views.home_page_view, name='home'),
    path('', views.home_page_view),
    path('apresentação', views.apresentacao_page_view, name='apresentação'),
    path('sobre', views.sobre_page_view, name='sobre'),
    path('projetos', views.projetos_page_view, name='projetos'),
    path('competencias', views.competencias_page_view, name='competencias'),
    path('blog', views.blog_page_view, name='blog'),
    path('nova/', views.view_novo_post, name='nova'),
    path('edita/<int:post_id>', views.view_editar_post, name='edita'),
    path('apaga/<int:post_id>', views.view_apagar_post, name='apaga'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('contacto', views.contacto_page_view, name='contacto'),
    path('web', views.web_page_view, name='web'),
    path('quizz', views.quizz_page_view, name='quizz'),
    path('login', views.login_page_view, name='login'),
    path('logout', views.logout_page_view, name='logout'),

]
