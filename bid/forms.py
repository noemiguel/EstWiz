# -*- coding: utf-8 -*-

from django.forms import ModelForm
from bid.models import Bid


class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['bid_subject','bid_body']