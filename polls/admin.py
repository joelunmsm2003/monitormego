from django.contrib import admin

# Register your models here.


#EJEMPLOSSSSSSSSSS......

 
from .models import *
from django.contrib import admin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter

from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

admin.site.register(Question)


@admin.register(Locales)
class localesAdmin(admin.ModelAdmin):

	list_display = ('nombre',)

@admin.register(Plataforma)
class plataformaAdmin(admin.ModelAdmin):

	list_display = ('nombre',)

@admin.register(LocalPlataforma)
class localPlataformaAdmin(admin.ModelAdmin):

	list_display = ('id',)

@admin.register(Estado)
class estadoAdmin(admin.ModelAdmin):

	list_display = ('tipo',)

@admin.register(Posicion)
class posicionAdmin(admin.ModelAdmin):


	list_display = ('localplataforma',)


@admin.register(Tiposicion)
class tiposicionAdmin(admin.ModelAdmin):


	list_display = ('tp', )

@admin.register(Interprete)
class interpreteAdmin(admin.ModelAdmin):
	list_display = ('nombre','apellido','dni')


@admin.register(Personal)
class personalAdmin(admin.ModelAdmin):
	list_display = ('nombre',)
	
@admin.register(Suplp)
class suplpAdmin(admin.ModelAdmin):
	list_display = ('nombre','localplataforma','nombre','idloc','idpl')




