from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('polls.urls')),
    url(r'^', include(admin.site.urls)),
]
