from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    uploadDate = models.DateTimeField()
    user = models.ForeignKey(User)
    
    def __str__(self):
        return self.name