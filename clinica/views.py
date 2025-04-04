from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Medico,Consulta


def listar_medicos(request):
    if request.method == 'GET':
        medicos = Medico.objects.all()
        return Response(medicos,status=status.HTTP_200_OK)
    return render (request,'listar_medicos.html')


def criar_consulta(request):
    if request.method == 'POST':
        pacientes = request.POST.get('paciente')
        data = request.POST.get('data')
        medico = request.POST.get('medico')
        estado = request.POST.get('status')
        Consulta.objects.create(pacientes=pacientes, data=data, medico=medico, status=estado)
        return Response( status=status.HTTP_201_CREATED)
    return render (request,'form_consulta.html')


def detalhes_consulta(request):
    if request.method == 'GET':
        consulta_info = Consulta.objects.all()
        return Response(consulta_info, status=status.HTTP_200_OK)
    return render(request, '')