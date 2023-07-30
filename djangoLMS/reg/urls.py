#from django.conf.urls import url
#the above is deprecated so replaced with re_path
from django.urls import re_path
from . import views
urlpatterns = [
    re_path(r'home/', views.home, name='reg-home'),
    re_path(r'^signup/$', views.signup, name='reg-signup'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    re_path(r'^login/$', views.login, name='login'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.reset, name='reset'),
    re_path(r'^logout/$', views.logout, name='logout'),
]
