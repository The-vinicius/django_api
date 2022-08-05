from django.test import TestCase
from django.urls import reverse
from ..models import Aluno

class AlunoTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.aluno = Aluno.objects.create(nome='god', serie='Y1')


    def test_model_content(self):
        self.assertEqual(self.aluno.nome, 'god')
        self.assertEqual(self.aluno.serie, 'Y1')
        
