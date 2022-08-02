from rest_framework import routers
from .views import hello_world, CreateAluno, CreateEscola
from django.urls import path

urlpatterns = [
    path('escola/', CreateEscola.as_view(), name='soll'),
    path('hello/', hello_world, name='hello'),
    path('aluno/', CreateAluno.as_view(), name='create'),
    path('alunos/<int:pk>', CreateAluno.as_view(), name='update'),
]
