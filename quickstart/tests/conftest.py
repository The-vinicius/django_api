from pytest import fixture
from ..models import Aluno

@fixture
def table_alunos():
    return Aluno.objects.all()


@fixture
def aluno_criado():
    return Aluno.objects.create(nome='vini', serie='Y3')

