from django.db import models

class Profile(models.Model):
    name=models.CharField(max_length=30)
    birthday=models.DateTimeField()
    horoscope=models.CharField(max_length=20)
