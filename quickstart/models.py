from django.db import models

class Aluno(models.Model):
    Choice_serie = (
        ('Y1', 'Primeiro ano'),
        ('Y2', 'Segundo ano'),
        ('Y3', 'Terceiro ano'),
    )
    nome = models.CharField(max_length=255)
    serie = models.CharField(max_length=2, choices=Choice_serie, default='Y1')


class Escola(models.Model):
    alunos = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
