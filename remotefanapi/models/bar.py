from django.db import models
from django.contrib.auth.models import User


class Bar(models.Model):

    name = models.CharField(max_length=75)
    city = models.ForeignKey("City", on_delete=models.CASCADE)
    address = models.CharField(max_length=100, default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    teams = models.ManyToManyField("Team", related_name="barTeams")

    @property
    def joined(self):
        """adds the property joined"""
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value
