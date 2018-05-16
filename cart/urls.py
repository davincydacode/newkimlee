from django.conf.urls import  include, url

from .import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$',views.index,name='index'),
     url(r'^admin/', views.admin, name='admin'),
     url(r'^uploadform/', views.uploadform, name='uploadform'),
     url(r'^viewproduct/',views.viewproduct,name='viewproduct'),
     url(r'^deleteproduct/',views.deleteproduct, name='deleteproduct'),
     url(r'^cartproduct/',views.cartproduct,name='cartproduct'),
     url(r'^cartitem/',views.cartitem,name='cartitem'),
     url(r'^updatecart/',views.updatecart,name='updatecart'),
   	  

    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^kimlee/', include('cart.urls')),


]

if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)