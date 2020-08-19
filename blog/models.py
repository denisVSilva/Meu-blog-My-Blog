from django.db import models

class pythonProjects(models.Model):
    Titulo = models.CharField(max_length=100)
    Descrição = models.TextField(max_length=250)
    Link = models.CharField(max_length=250)

    def __str__(self):
        return self.Titulo
    
class blenderProjects(models.Model):
    Titulo = models.CharField(max_length=100)
    Descrição = models.TextField(max_length=250)
    Link = models.CharField(max_length=250)
    imagen = models.CharField(max_length=250)

    def __str__(self):
        return self.Titulo
    