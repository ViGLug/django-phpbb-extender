from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(
        regex=r'^topic/',
        view=views.Topics.as_view(),
        name='topics'
    ),
)