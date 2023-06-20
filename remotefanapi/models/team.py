from django.db import models

class Team(models.Model):

    name = models.CharField(max_length=50)
    city = models.ForeignKey("City", on_delete=models.CASCADE)
    sport = models.ForeignKey("Sport", on_delete=models.CASCADE)
    bars = models.ManyToManyField("Bar", related_name="teamBars")
    logo = models.URLField(blank=True)
