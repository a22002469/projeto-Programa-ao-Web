from django.urls import path
from . import views

app_name = 'portfolio'
name = 'home'
urlpatterns = [
    path('home', views.home_page_view, name='home'),
    path('', views.home_page_view),
]
