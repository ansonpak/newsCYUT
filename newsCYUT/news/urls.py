from django.conf.urls import url
from news import views

urlpatterns = [
    url(r'^$', views.news, name='news'),
    url(r'^latestnews/(?P<latestnewsID>[0-9]+)/$', views.latestnews, name='latestnews'),
]