from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(
        regex=r'^rss/post/$',
        view=views.PostsRSS(),
        name='posts_rss'
    ),
    url(
        regex=r'^atom/post/$',
        view=views.PostsAtom(),
        name='posts_atom'
    ),
    url(
        regex=r'^rss/topic/$',
        view=views.TopicsRSS(),
        name='topics_rss'
    ),
    url(
        regex=r'^atom/topic/$',
        view=views.TopicsAtom(),
        name='topics_atom'
    ),
)