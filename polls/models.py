from __future__ import unicode_literals
from django.forms import ModelForm
from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.
# Create your models here.

from django.utils.encoding import python_2_unicode_compatible

import datetime

from django.utils import timezone


from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


# Create your models here.

@python_2_unicode_compatible
class Locales(models.Model):
  
    nombre = models.CharField(max_length=300,blank=True)

    def __str__(self):

        return self.nombre
    class Meta:
        managed = True
        verbose_name = 'Locale'

@python_2_unicode_compatible
class Nivel(models.Model):
  
    nombre = models.CharField(max_length=300,blank=True)

    def __str__(self):

        return self.nombre
    class Meta:
        managed = True
        verbose_name = 'Nivel'



@python_2_unicode_compatible
class Plataforma(models.Model):
  
    nombre = models.CharField(max_length=300,blank=True)

    def __str__(self):

        return self.nombre

@python_2_unicode_compatible
class LocalPlataforma(models.Model):
  
    local = models.ForeignKey(Locales,related_name='LocalPlataforma',max_length=300,blank=True,null=True)
    plataforma = models.ForeignKey(Plataforma,max_length=300,blank=True,null=True)


    def __str__(self):

        return str(self.local.nombre)+'-'+str(self.plataforma.nombre)

    class Meta:
        managed = True
        verbose_name = 'Local Plataforma'

@python_2_unicode_compatible
class Estado(models.Model):
  
    tipo = models.CharField(max_length=300,blank=True)


    class Meta:
        managed = True
        verbose_name = 'Estado'


    def __str__(self):

        return self.tipo


@python_2_unicode_compatible
class Tiposicion(models.Model):
  
    tp = models.CharField(max_length=300,blank=True)

    class Meta:
        managed = True
        verbose_name = 'Tipo de Posicion'

    def __str__(self):
        return self.tp


@python_2_unicode_compatible
class Color(models.Model):

    nombre = models.CharField('Color',max_length=300,blank=True)
   
    class Meta:
        managed = True
        verbose_name = 'Color'

    def __str__(self):
        return self.nombre 


@python_2_unicode_compatible
class Personal(models.Model):

    nombre = models.CharField('Estado Interprete',max_length=300,blank=True)
    color = models.ForeignKey(Color,max_length=300,blank=True,null=True)
   
    class Meta:
        managed = True
        verbose_name = 'Estado de Cubiculo'

    def __str__(self):
        return self.nombre 


@python_2_unicode_compatible
class Interprete(models.Model):

    nombre = models.CharField(max_length=300,null=True,blank=True)
    apellido = models.CharField(max_length=300,blank=True,null=True)
    dni = models.CharField(max_length=300,blank=True,null=True)
    iden = models.CharField('ID',max_length=300,null=True,blank=True)
    local = models.ForeignKey(Locales,max_length=300,blank=True,null=True)
    nivel = models.ForeignKey(Nivel,max_length=300,blank=True,null=True)

    def __str__(self):

         return self.nombre

@python_2_unicode_compatible
class Posicion(models.Model):
  
    localplataforma = models.ForeignKey(LocalPlataforma,max_length=300,blank=True,null=True)
    tipo = models.ForeignKey(Tiposicion,max_length=300,blank=True,null=True)
    estado_personal= models.ForeignKey(Personal,max_length=300,blank=True,null=True)
    interprete= models.ForeignKey(Interprete,max_length=300,blank=True,null=True)
    estado_maquina= models.ForeignKey(Estado,max_length=300,blank=True,null=True)
    nombre = models.CharField(max_length=300,blank=True)

    class Meta:
        managed = True
        verbose_name = 'Cubiculo'
    
    def __str__(self):
        return self.localplataforma.local.nombre


@python_2_unicode_compatible
class Suplp(models.Model):
  
    localplataforma = models.ForeignKey(LocalPlataforma,max_length=300,blank=True,null=True)
    nombre = models.CharField(max_length=300,blank=True)
    idloc = models.ForeignKey(Locales,max_length=300,blank=True)
    idpl= models.ForeignKey(Plataforma,max_length=300,blank=True)
    def __str__(self):
        return self.idlop

    class Meta:
        managed = True
        verbose_name = 'Supervisor Plataforma'








