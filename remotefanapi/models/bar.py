from django.db import models

class Bar(models.Model):

    name = models.CharField(max_length=75)
    city = models.ForeignKey("City", on_delete=models.CASCADE)
    owner = models.ForeignKey("User", on_delete=models.CASCADE)
    teams = models.ManytoManyField("Team")