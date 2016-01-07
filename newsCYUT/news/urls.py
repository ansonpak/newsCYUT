from django.conf.urls import url
from news import views

urlpatterns = [
    url(r'^latestnews/(?P<latestnewsID>[0-9]+)/$', views.latestnews, name='latestnews'),
    url(r'^addLatestnews/$', views.addLatestnews, name='addLatestnews'),
    url(r'^deleteLatestnews1/$', views.deleteLatestnews1, name='deleteLatestnews1'),
    url(r'^deleteLatestnews/(?P<latestnewsID>[0-9]+)/$', views.deleteLatestnews, name='deleteLatestnews'),
    url(r'^updateLatestnews/(?P<latestnewsID>[0-9]+)/$', views.updateLatestnews,
 name='updateLatestnews'),
    url(r'^$', views.news, name='news'),
]