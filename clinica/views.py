from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Medico,Consulta

@api_view(['GET'])
def listar_medicos(request):
    medicos = Medico.objects.all()
    return medicos

@api_view(['POST'])
def criar_consulta(request):
        pacientes = request.POST.get('paciente')
        data = request.POST.get('data')
        medico = request.POST.get('medico')
        status = request.POST.get('status')
        Consulta.objects.create(pacientes = pacientes, data=data, medico=medico, status=status)
        return Response({'Criado com Sucesso!'}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def detalhes_consulta(request):
    consulta_info = Consulta.objects.all()
    return consulta_info