from django.conf.urls import  include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns =[
    # Examples:
    # url(r'^$', 'kimlee.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^kimlee/', include('cart.urls')),


] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
#	urlpatterns += [url(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT,}),]

#if settings.DEBUG:
#	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
