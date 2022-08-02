from rest_framework.views import APIView
from quickstart.models import Aluno, Escola
from rest_framework.decorators import api_view
from quickstart.serializers import AlunoSerializer, EscolaSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class CreateEscola(APIView):
    serializer_class = EscolaSerializer



class CreateAluno(APIView):
    serializer_class = AlunoSerializer


    def get(self, request):
        alunos = Aluno.objects.all()
        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def post(self, request):
        data = {
            'nome': request.data.get('nome'),
            'serie': request.data.get('serie'),
        }
        serializer = AlunoSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        salve_aluno = get_object_or_404(Aluno.objects.all(), pk=pk)
        data = {
            'nome': request.data.get('nome'),
            'serie': request.data.get('serie'),
        }
        serializer = AlunoSerializer(salve_aluno, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        aluno = get_object_or_404(Aluno.objects.all(), pk=pk)
        aluno.delete()
        return Response({'messages':'deleted'})



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

