from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(
        regex=r'^post/$',
        view=views.Posts.as_view(),
        name='posts'
    ),
    url(
        regex=r'^topic/$',
        view=views.Topics.as_view(),
        name='topics'
    ),
)