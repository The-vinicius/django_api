from rest_framework.views import APIView
from quickstart.models import Aluno, Escola
from rest_framework.decorators import api_view
from quickstart.serializers import AlunoSerializer, Escola
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def aluno_all(request):
    if request.method == 'POST':
        alunos = Aluno.objects.all()
        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data)


@api_view(['POST', 'GET'])
def hello_world(request):
    if request.method == 'POST':
        data = {
            'nome': request.data.get('nome'),
            'serie': request.data.get('serie'),
        }
        serializer = AlunoSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"message": "Got some data!", "data": request.data})
    if request.method == 'GET':
            alunos = Aluno.objects.all()
            serializer = AlunoSerializer(alunos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

