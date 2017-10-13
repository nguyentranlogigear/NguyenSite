# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegisterForm


def base(request):
	return render(request, 'movies/user/base.html', {})

def home(request):
	return render(request, 'movies/user/index.html',{})

def film(request):
	return render(request, 'movies/user/film.html',{})

def login(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(email=email, password=raw_password)
			login(request, user)
			return redirect('index')
	else:
		form = UserCreationForm()
	return render(request, 'movies/user/login-register.html',{'form':form})

def logout(request):
	return render(request, 'movies/user/film-detail.html',{})

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data.get('name')
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')
			confirm_pass = form.cleaned_data.get('confirm_pass')
			if not (
				User.objects.filter(username=username).exists() or
				User.objects.filter(email=email).exists()
				):
			User.objects.create_user(username, name, email, password, confirm_pass, phone, birthday)

			user = authenticate(username = username, password = password)
			login(request, user)
			return HttpResponseRedirect('/')


	return render(request, 'movies/user/film-detail.html',{})

def film_detail(request):
	return render(request, 'movies/user/film-detail.html',{})

	