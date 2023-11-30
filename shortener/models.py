from django.db import models

# Create your models here.
class Url(models.Model):
    url = models.CharField(max_length=1000)
    url_code = models.CharField(max_length=4)

    def __str__(self):
        return self.url
    
