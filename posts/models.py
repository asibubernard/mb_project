from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField()

    def __str__(self):  # text as string
        return self.text[:50] 
