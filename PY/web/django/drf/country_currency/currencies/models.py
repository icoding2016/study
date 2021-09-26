from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=30)
    currency = models.CharField(max_length=20)
    time = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

