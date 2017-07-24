from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from views import IndexView

urlpatterns = [
    url(r'^$', view=IndexView.as_view(), name='index'),
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^lunch/', include('lunchpot.urls')),
]
