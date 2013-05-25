from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(
        regex=r'^post/$',
        view=views.PostsRSS(),
        name='posts_rss'
    ),
)