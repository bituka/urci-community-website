from django.db import models

class Announcement(models.Model):
    announcement_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')