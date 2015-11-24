from django.conf.urls import url
from photo import views

urlpatterns = [
    url(r'^$', views.photo, name='photo'),
]