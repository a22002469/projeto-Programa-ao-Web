from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Quizz
from .models import Projetos
from .models import Cadeiras
from .models import Sobre
from .models import Web

admin.site.register(Post)
admin.site.register(Quizz)
admin.site.register(Projetos)
admin.site.register(Cadeiras)
admin.site.register(Sobre)
admin.site.register(Web)

