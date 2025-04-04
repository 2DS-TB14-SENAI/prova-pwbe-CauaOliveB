from django.db import models

class Medico(models.Model):
    nome = models.CharField(max_length=100, )
    choices = [
        ("CAR","Cardiologista"),
        ("ORT", "Ortopedista"),
        ("NEU", "Neurologita"),
        ("END", "Endocrinologista"),
        ("PSI", "Psiquiatria"),
    ]
    especialidade = models.CharField(max_length=3, choices=choices)
    crm = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=254, blank=True, null=True)

class Consulta(models.Model):
    paciente = models.CharField(max_length=100)
    data = models.DateTimeField( auto_now=False, auto_now_add=False)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    choices = [
        ("AGEN","agendado"), 
        ("REAL","realizado"), 
        ("CANC","cancelado"),
    ]

    status = models.CharField(max_length=4, choices=choices)