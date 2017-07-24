from django.conf.urls import patterns, url
from lunchpot import views


urlpatterns = patterns(
    '',
    url(r'^$',
        view=views.DashboardView.as_view(),
        name='dashboard'
        ),
)
