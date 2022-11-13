from django.conf import settings
from django.conf.urls.defaults import include, patterns, url
from django.contrib import admin
from django.urls import path

from . import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('myapp.cesar.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns = [
    path('',views.home_page,name="main_home" )

]
if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )