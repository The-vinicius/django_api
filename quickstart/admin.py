from django.contrib import admin
from .models import Aluno

@admin.register(Aluno)
class NotaAdmin(admin.ModelAdmin):
    pass
