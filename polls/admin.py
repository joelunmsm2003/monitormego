from django.contrib import admin

# Register your models here.


#EJEMPLOSSSSSSSSSS......

 
from .models import *
from django.contrib import admin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter

from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

# admin.site.register(Question)

admin.site.site_header = 'Monitoreo Interprete'


@admin.register(Nivel)
class localesAdmin(admin.ModelAdmin):

	list_display = ('id','nombre',)


@admin.register(Locales)
class localesAdmin(admin.ModelAdmin):

	list_display = ('id','nombre',)

@admin.register(Plataforma)
class plataformaAdmin(admin.ModelAdmin):

	list_display = ('id','nombre',)

@admin.register(LocalPlataforma)
class localPlataformaAdmin(admin.ModelAdmin):

	list_display = ('id','local','plataforma')
	list_filter = ('local__nombre',)



@admin.register(Estado)
class estadoAdmin(admin.ModelAdmin):

	list_display = ('tipo',)

@admin.register(Posicion)
class posicionAdmin(admin.ModelAdmin):


	list_display = ('nombre','localplataforma','tipo','interprete','estado_maquina','estado_personal')
	list_filter = ('localplataforma',)


@admin.register(Tiposicion)
class tiposicionAdmin(admin.ModelAdmin):


	list_display = ('tp', )

@admin.register(Interprete)
class interpreteAdmin(admin.ModelAdmin):
	list_display = ('nombre','apellido','dni','iden','sede')
	list_filter=('local__nombre',)

	def sede(self, obj):
		return obj.local.nombre


@admin.register(Personal)
class personalAdmin(admin.ModelAdmin):
	list_display = ('nombre',)
	
@admin.register(Suplp)
class suplpAdmin(admin.ModelAdmin):
	list_display = ('nombre','localplataforma','nombre','idloc','idpl')




