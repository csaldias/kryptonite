# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-13 23:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bentobox', '0004_auto_20170612_1211'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_aprendizaje', models.CharField(choices=[('ad', 'Adaptador'), ('di', 'Divergente'), ('co', 'Convergente'), ('as', 'Asimilador')], default='ad', max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]