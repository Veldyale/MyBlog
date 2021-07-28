from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=300)
    date = models.DateTimeField()
    text = models.TextField()
    image = models.FileField(upload_to='blog_images/')
    # file = models.FileField(upload_to='pdf_files/')

