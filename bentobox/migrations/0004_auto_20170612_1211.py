# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-12 16:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bentobox', '0003_auto_20170612_1208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contenido',
            old_name='valid',
            new_name='aprobado',
        ),
        migrations.RenameField(
            model_name='contenido',
            old_name='clasif_ad',
            new_name='clasificacion_adaptador',
        ),
        migrations.RenameField(
            model_name='contenido',
            old_name='clasif_as',
            new_name='clasificacion_asimilador',
        ),
        migrations.RenameField(
            model_name='contenido',
            old_name='clasif_co',
            new_name='clasificacion_convergente',
        ),
        migrations.RenameField(
            model_name='contenido',
            old_name='clasif_di',
            new_name='clasificacion_divergente',
        ),
        migrations.RenameField(
            model_name='contenido',
            old_name='desc',
            new_name='descripcion',
        ),
    ]
