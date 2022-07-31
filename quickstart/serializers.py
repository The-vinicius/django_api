from rest_framework import serializers
from .models import Aluno, Escola


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ('nome', 'serie')


class EscolaSerializer(serializers.ModelSerializer):
    alunos = AlunoSerializer(many=True, required=False)

    class Meta:
        model = Escola
        fields = ('nome', 'alunos')
