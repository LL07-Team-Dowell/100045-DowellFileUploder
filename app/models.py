from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    folder = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Video(models.Model):
    video = models.FileField(upload_to='videos/')
    folder = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
