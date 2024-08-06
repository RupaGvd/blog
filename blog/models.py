from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=20)
    img = models.ImageField(upload_to='photos',blank=True)
    desc = models.TextField(max_length=350)

    def __str__(self):
        return self.title


