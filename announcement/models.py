from django.db import models
from django.urls import reverse
# Create your models here.

class Announcement(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=100, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        
        return reverse('announcement:single', kwargs={'pk':self.pk})