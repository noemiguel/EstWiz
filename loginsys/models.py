from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=8)
    email = models.EmailField(max_length=40, blank=True)
    password = models.CharField(max_length=100)


    def __str__(self):
        return self.name