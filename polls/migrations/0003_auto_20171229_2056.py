# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-29 20:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20171229_2050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='localplataforma',
            name='nomlocal',
        ),
        migrations.RemoveField(
            model_name='localplataforma',
            name='nomplat',
        ),
        migrations.AddField(
            model_name='localplataforma',
            name='local',
            field=models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.locales'),
        ),
        migrations.AddField(
            model_name='localplataforma',
            name='plataforma',
            field=models.ForeignKey(blank=True, max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.plataforma'),
        ),
    ]