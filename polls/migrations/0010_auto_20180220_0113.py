# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-20 01:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20180220_0107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=300)),
            ],
            options={
                'verbose_name': 'Nivel',
                'managed': True,
            },
        ),
        migrations.AlterField(
            model_name='interprete',
            name='local',
            field=models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Locales'),
        ),
        migrations.AlterField(
            model_name='localplataforma',
            name='local',
            field=models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='LocalPlataforma', to='polls.Locales'),
        ),
        migrations.AlterField(
            model_name='localplataforma',
            name='plataforma',
            field=models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Plataforma'),
        ),
        migrations.AlterField(
            model_name='posicion',
            name='estado_maquina',
            field=models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Estado'),
        ),
        migrations.AlterField(
            model_name='posicion',
            name='estado_personal',
            field=models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Personal'),
        ),
        migrations.AlterField(
            model_name='posicion',
            name='interprete',
            field=models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Interprete'),
        ),
        migrations.AlterField(
            model_name='posicion',
            name='localplataforma',
            field=models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.LocalPlataforma'),
        ),
        migrations.AlterField(
            model_name='posicion',
            name='tipo',
            field=models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Tiposicion'),
        ),
        migrations.AlterField(
            model_name='suplp',
            name='idloc',
            field=models.ForeignKey(blank=True, max_length=300, on_delete=django.db.models.deletion.CASCADE, to='polls.Locales'),
        ),
        migrations.AlterField(
            model_name='suplp',
            name='idpl',
            field=models.ForeignKey(blank=True, max_length=300, on_delete=django.db.models.deletion.CASCADE, to='polls.Plataforma'),
        ),
        migrations.AlterField(
            model_name='suplp',
            name='localplataforma',
            field=models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.LocalPlataforma'),
        ),
    ]
