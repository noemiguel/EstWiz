from django.db import models
from loginsys.models import Author
from django.contrib.auth.models import User

class Bid(models.Model):
    bid_subject = models.CharField(max_length=100)
    bid_body = models.TextField(max_length=500)
    bid_author = models.ForeignKey(User, null=True)
    #bid_date = models.DateTimeField.auto_now

    def __str__(self):
        return self.bid_subject