from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.static import * 
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^simpleBlog/', include('simpleBlog.urls')),
	url(r'^admin/', include(admin.site.urls)),
	#url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	
)


#if not settings.DEBUG:
urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)