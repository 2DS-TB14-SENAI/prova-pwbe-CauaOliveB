from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Medico,Consulta

@api_view(['GET'])
def listar_medicos(request):
    return Medico

@api_view(['POST'])
def criar_consulta(request):
        pacientes = request.POST.get('paciente')
        data = request.POST.get('data')
        medico = request.POST.get('medico')
        status = request.POST.get('status')
        return Response({'Criado com Sucesso!'}, status=status.HTTP_201_CREATED)



        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        Tarefa.objects.create(titulo=titulo, descricao=descricao)
        return redirect('listar_tarefas')

@api_view(['GET'])
def detalhes_consulta(request):
    return Consulta