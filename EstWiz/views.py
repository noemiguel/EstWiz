# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.contrib import auth


def home(request):
    args = {}
    args['username'] = auth.get_user(request).username
    return render_to_response('homepage.html', args)