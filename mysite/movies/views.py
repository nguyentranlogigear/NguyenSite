# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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
from .models import Profile

def base(request):
	return render(request, 'movies/base.html', {})

def home(request):
	return render(request, 'movies/home.html',{'section' : 'home'})

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
			return render(request,'movies/home.html', {})
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
 			profile = Profile.object.create(user=new_user)

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


def film_detail(request):
	return render(request, 'movies/film-detail.html',{})


	