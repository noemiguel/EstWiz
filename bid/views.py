# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from bid.models import Bid
from bid.forms import BidForm

def bid_form(request):
    args = {}
    args.update(csrf(request))
    args['form'] = BidForm
    args['username'] = auth.get_user(request).username
    return render_to_response('bid_form.html', args)

def bid_form_submit(request):
    user = auth.get_user(request)
    if user.is_authenticated():
        if request.POST:
            bsubj = request.POST.get('bidsubject','')
            bbody = request.POST.get('bidbody','')
            new_bid = Bid(
                bid_subject = bsubj,
                bid_body = bbody,
                bid_author = user
            )
            new_bid.save()
            return render_to_response('form_is_submitted.html', {'username': auth.get_user(request).username})
    else:
        return render_to_response('bid_form.html', {'error': "Вы не вошли"})

def bid(request, bid_id):
    args = {}
    args.update(csrf(request))
    args['bid'] = Bid.objects.get(id = bid_id)
    args['name'] = "bid"
    args['username'] = auth.get_user(request).username
    return render_to_response('bid.html', args )

def bid_list(request):
    args = {}
    args.update(csrf(request))
    author = auth.get_user(request)
    args['bids'] = Bid.objects.filter(bid_author_id=author.id)
    args['username'] = auth.get_user(request).username
    return render_to_response('list.html', args)