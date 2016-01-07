from django.conf.urls import url
from photo import views

urlpatterns = [
    url(r'^$', views.photobook, name='photobook'),
    url(r'^album/(?P<albumID>[0-9]+)/$', views.album, name='album'),
    url(r'^photo/(?P<photoID>[0-9]+)/$', views.photo, name='photo'),
    url(r'^addAlbum/$', views.addAlbum, name='addAlbum'),
    url(r'^addPhoto/(?P<albumID>[0-9]+)/$', views.addPhoto, name='addPhoto'),
    url(r'^deleteAlbum1/$', views.deleteAlbum1, name='deleteAlbum1'),
    url(r'^deleteAlbum/(?P<albumID>[0-9]+)/$', views.deleteAlbum,name='deleteAlbum'),
    url(r'^deletePhoto1/$', views.deletePhoto1, name='deletePhoto1'),
    url(r'^deletePhoto/(?P<photoID>[0-9]+)/$', views.deletePhoto,name='deletePhoto'),
    url(r'^updateAlbum/(?P<albumID>[0-9]+)/$', views.updateAlbum,name='updateAlbum'),
    url(r'^updatePhoto/(?P<photoID>[0-9]+)/$', views.updatePhoto,name='updatePhoto'),
]