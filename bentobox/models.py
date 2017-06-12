from django.db import models

# Create your models here.
class Contenido(models.Model):
    tipos_contenido = (
    ('sd', 'Sin Definir'),
    ('ad', 'Adaptador'),
    ('di', 'Divergente'),
    ('co', 'Convergente'),
    ('as', 'Asimilador'),
    )
    link = models.URLField(max_length=1024)
    desc = models.CharField(max_length=200)
    #TODO: Faltan los TAG's!
    clasif = models.CharField(max_length=2,
                              choices = tipos_contenido,
                              default = 'sd')
    valid = models.BooleanField()

    def __str__(self):
        return self.link
