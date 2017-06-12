from django.db import models

# Create your models here.
class Contenido(models.Model):
    ptje = (
    (0, 'No relevante'),
    (1, 'Relevante'),
    (2, 'Muy relevante'),
    )

    link = models.URLField(max_length=1024)
    descripcion = models.CharField(max_length=200)
    tags = models.CharField(max_length=2048)
    clasificacion_adaptador = models.IntegerField(choices = ptje,default = 1)
    clasificacion_divergente = models.IntegerField(choices = ptje,default = 1)
    clasificacion_convergente = models.IntegerField(choices = ptje,default = 1)
    clasificacion_asimilador = models.IntegerField(choices = ptje,default = 1)
    aprobado = models.BooleanField()

    def __str__(self):
        return self.link+" - "+self.descripcion
