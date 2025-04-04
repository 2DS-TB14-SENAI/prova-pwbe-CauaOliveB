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
    pacientes = request.data.get('paciente')
    data = request.data.get('data')
    medico = request.data.get('medico')
    status = request.data.get('status')

    