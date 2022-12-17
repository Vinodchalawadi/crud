from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=50)
    role  = models.CharField(max_length=20)
    company = models.CharField(max_length=20)
    about = models.CharField(max_length=100)
    active =models.BooleanField(default=True)

    def __str__(self):
        return self.name

