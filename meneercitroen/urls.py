from django.conf.urls import include, url
from django.contrib import admin

from views import index

urlpatterns = [
    url(r'^$', view=index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^lunch/', include('lunchpot.urls')),
]
