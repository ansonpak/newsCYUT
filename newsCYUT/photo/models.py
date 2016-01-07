from django.db import models

# Create your models here.
class Album(models.Model):
    photourl = models.URLField()
    albumtitle = models.CharField(max_length=128)

    def __str__(self):
        return self.albumtitle
    
class Photo(models.Model):
    album = models.ForeignKey(Album)
    url = models.URLField()
    index = models.TextField()

    def __str__(self):
        return self.id