from django.db import models

# Create your models here.
class Document(models.Model):
    doc_title = models.CharField(max_length=200)
    doc_link = models.CharField(max_length=200)