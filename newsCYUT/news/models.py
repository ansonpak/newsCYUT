from django.db import models


# Create your models here.
class Latestnews(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    uploadDate = models.DateField() 

    
    def __str__(self):
        return self.title