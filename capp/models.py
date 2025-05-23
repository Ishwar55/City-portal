from django.db import models

# Create your models here.
# capp/models.py

class HomepageImage(models.Model):
    image = models.ImageField(upload_to='homepage_images/')
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description


