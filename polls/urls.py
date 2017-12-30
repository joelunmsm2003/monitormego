from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^posiciones', views.posiciones),
    ]