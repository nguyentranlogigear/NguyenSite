# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
import datetime

def home(request):
	#return render(request, 'movies/index.html',)
	now = datetime.datetime.now()
	return render(request, 'movies/layouts/index.html', {})
