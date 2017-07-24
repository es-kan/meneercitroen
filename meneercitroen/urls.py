from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from views import index

urlpatterns = [
    url(r'^$', view=index, name='index'),
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^lunch/', include('lunchpot.urls')),
]
