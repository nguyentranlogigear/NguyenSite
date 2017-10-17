# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserLoginForm,UserRegisterForm, UserEditForm, ProfileEditForm
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from .models import Profile, Category, Director, Actor, Promotion, Film, Showtime, Showtime_Detail


def home(request):
	promotions = Promotion.objects.all().order_by('-created_at')[:5]

	return render(request, 'movies/home.html',{'section' : 'home', 'promotions': promotions})

def film(request):
	return render(request, 'movies/film.html',{})

def user_login(request):
	if request.method == 'POST':
		form = UserLoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username=cd['username'],
								password=cd['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return render(request,'movies/home.html', {})
				else:
					return render(request, 'registration/login.html',{'errors': 'Your account is block'})
			else:
				return render(request,'registration/login.html', {'errors': 'Username and password is correct.Please try again'})
	else:
		if request.user.is_authenticated():
			promotions = Promotion.objects.all().order_by('-created_at')[:5]
			return render(request,'movies/home.html', {'promotions': promotions})
		else:
			form = UserLoginForm()
	return render(request, 'registration/login.html',{'form':form})

@login_required
def logout(request):
	django_logout(request)
	return render(request, 'movies/home.html', {})

def register(request):
 	if request.method == 'POST':
 		form = UserRegisterForm(request.POST)
 		if form.is_valid():
 			# Create a new user object but avoid saving it yet
 			new_user = form.save(commit=False)

 			# Set the choosen password
 			new_user.set_password(form.cleaned_data['password'])

 			# Save the user object
 			new_user.save()

 			# Create the user profile
 			profile = Profile.objects.create(user=new_user)

 			return render(request, 'registration/register_done.html', {'new_user':new_user})

 	else:
 		form = UserRegisterForm()

 	return render(request, 'registration/register.html', {'form':form })

@login_required
def edit_profile(request):
	if request.method == 'POST':
		user_form = UserEditForm(
			instance=request.user, 
			data=request.POST 
			)
		profile_form = ProfileEditForm(
			instance=request.user.profile, 
			data=request.POST, 
			files=request.FILES
			)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
	else:
		user_form = UserEditForm(instance=request.user)
		profile_form = ProfileEditForm(instance=request.user.profile)
	return render(request, 
			'account/edit_profile.html',
			{'user_form': user_form,
			'profile_form': profile_form })


def film_detail(request, id):
	try:
		film = Film.objects.get(pk=id)
		return render(request, 'movies/film-detail.html',{'film':film})

	except Film.DoesNotExist:
		raise Http404('Films does not exist')


def promotion_detail(request, id):
	try:
		promotion = Promotion.objects.filter(id = id).order_by('-created_at')

	except Promotion.DoesNotExist:
		raise Http404('Promotion does not exist')

	return render(request, 'movies/promotion_detail.html', {'promotion':promotion })


def film_showing(request):

	list_film_show = Film.objects.filter(status = 'NR')

	return render(request, 'movies/film_showing.html', {'list_film_show': list_film_show })

def uncoming_movies(request):
	list_uncoming_movies = Film.objects.filter(status='NS')

	return render(request, 'movies/uncoming_movies.html', {'list_uncoming_movies': list_uncoming_movies})

	