from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^posiciones/(\d+)', views.posiciones),
        url(r'^plataforma/(\d+)', views.plataforma),
        url(r'^cargapersonal/(\d+)', views.cargapersonal),

        
    ]


    