from django.contrib import admin
from django.shortcuts import *
from django.template import RequestContext
from django.contrib.auth import *
from django.contrib.auth.models import Group, User
from django.contrib.sessions.models import Session
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.core.urlresolvers import reverse
from django.db.models import Max,Count
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpRequest
# Register your models here.


#EJEMPLOSSSSSSSSSS......

 
from .models import *
from django.contrib import admin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter

from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

# admin.site.register(Question)

admin.site.site_header = 'Monitoreo Interprete'


class DecadeBornListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title ='Cubiculos'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'Usuario'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('X', 'X'),
            # ('90s', 'in the nineties'),
        )

    def queryset(self, request, queryset):
		"""
		Returns the filtered queryset based on the value
		provided in the query string and retrievable via
		`self.value()`.
		"""
		# Compare the requested value (either '80s' or '90s')
		# to decide how to filter the queryset.


		#if self.value() == '80s':
		# print queryset

		grupo = User.objects.get(pk=request.user.id).groups.get()


		print type(grupo)

		if str(grupo)=='Admin':

			return queryset.all()
			
		else:

			return queryset.filter(localplataforma__supervisor__user_id=request.user.id)


		# if self.value() == '90s':
		#     return queryset.all()


@admin.register(Posicion)
class posicionAdmin(admin.ModelAdmin):


	list_display = ('nombre','localplataforma','tipo','interprete','estado_maquina','estado_personal')
	list_filter = (DecadeBornListFilter,)




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



@admin.register(Tiposicion)
class tiposicionAdmin(admin.ModelAdmin):


	list_display = ('tp', )

@admin.register(Interprete)
class interpreteAdmin(admin.ModelAdmin):
	list_display = ('nombre','apellido','dni','iden','sede')
	list_filter=('local__nombre',)

	def sede(self, obj):
		return obj.local.nombre


@admin.register(Supervisor)
class supervisorAdmin(admin.ModelAdmin):
	list_display = ('nombre','apellido','dni')


	def sede(self, obj):
		return obj.local.nombre

@admin.register(Personal)
class personalAdmin(admin.ModelAdmin):
	list_display = ('nombre',)
	
@admin.register(Suplp)
class suplpAdmin(admin.ModelAdmin):
	list_display = ('supervisor','localplataforma')




