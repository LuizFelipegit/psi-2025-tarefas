from django.db import models

class Tarefa(models.Model):
    nome = models.CharField(max_length=200)
    status = models.CharField(max_length=20)  
    prazo = models.DateField()

    def _str_(self):
        return self.nome