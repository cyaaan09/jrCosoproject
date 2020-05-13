# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

from time import gmtime, strftime
from django.contrib import messages
from django.utils.crypto import get_random_string

# Create your views here.

def index(request):
    # response = "Hello, I am your first request!"
    return render(request, 'thesis/index.html') 
