from rest_framework.views import APIView
from quickstart.models import Aluno, Escola
from rest_framework.decorators import api_view
from quickstart.serializers import AlunoSerializer, EscolaSerializer
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.http import JsonResponse
from django.core import serializers

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

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

def hello_cache(request):
    if 'alunos' in cache:
        # get results from cache
        alunos = cache.get('alunos')
        print(alunos)
        return JsonResponse(alunos, safe=False)
 
    else:
        alunos  = Aluno.objects.all()
        results = serializers.serialize('json', alunos)
        print(results)
        # store data in cache
        cache.set('alunos', results, timeout=CACHE_TTL)
        return JsonResponse(results, safe=False)

def sample(request):
    objs = Aluno.objects.all()
    json = serializers.serialize('json', objs)
    return JsonResponse(json, safe=False)
