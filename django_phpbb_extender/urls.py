from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_phpbb_extender.views.home', name='home'),
    # url(r'^django_phpbb_extender/', include('django_phpbb_extender.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^api/', include('api.urls')),
    url(r'^feed/', include('feed.urls')),
    url(r'^mobile/', include('mobile.urls')),
)
