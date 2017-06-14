from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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

class Categoria(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipos_aprendizaje = (
    ('ad', 'Adaptador'),
    ('di', 'Divergente'),
    ('co', 'Convergente'),
    ('as', 'Asimilador'),
    )
    tipo_aprendizaje = models.CharField(max_length=2, choices=tipos_aprendizaje, default='ad')

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Categoria.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.categoria.save()
