from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=300)
    date = models.DateTimeField()
    text = models.TextField()
    image = models.FileField(upload_to='blog_images/')
    # file = models.FileField(upload_to='pdf_files/')


    def get_summary(self):
        if len(self.text) > 35:
            return self.text[:35] + ' ...'
        else:
            return self.text

    def __str__(self):
        return self.title
