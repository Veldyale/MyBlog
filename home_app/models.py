from django.db import models

class Home(models.Model):
    home_image = models.ImageField(upload_to='home_images/')
    home_text = models.CharField(max_length=300)

