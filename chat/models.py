# Create your models here.

from django.db import models

class Message(models.Model):
    message_text = models.CharField(max_length=200)
    message_date = models.DateTimeField("date published")
    sender = models.CharField(max_length=200, default="Anonymous")
