from django.db import models

class Sport(models.Model):

    label = models.CharField(max_length=50)
