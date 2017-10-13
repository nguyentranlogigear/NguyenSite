# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit import ImageSpec, register
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from phonenumber_field.modelfields import PhoneNumberField

class Category(models.Model):
	name = models.CharField(max_length=250)
	symbol = models.CharField(max_length=250)

	def __unicode__(self):
		return self.name

class Director(models.Model):
	name = models.CharField(max_length=250)

	def __unicode__(self):
		return self.name

class Actor(models.Model):
	name = models.CharField(max_length=250)

	def __unicode__(self):
		return self.name

class Promotion(models.Model):
	name = models.CharField(max_length=250)
	title = models.CharField(max_length=500)
	image = ProcessedImageField(
		upload_to='movies/static/movies/images/promotion/%Y/%m/%d',
        processors=[ResizeToFill(263, 263)],
        format='PNG',
        options={'quality': 60})

	description = RichTextUploadingField()
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	ACTIVE = (
		(1, u'Active'),
		(2, u'Block'),
		)
	is_active = models.IntegerField(choices=ACTIVE, default=1)

	def __unicode__(self):
		return self.name

class Film(models.Model):
	category = models.ManyToManyField(Category, through='FilmCategory')
	director = models.ManyToManyField(Director, through='FilmDirector')
	actor = models.ManyToManyField(Actor, through='FilmActor')
	name = models.CharField(max_length=250)
	image = ProcessedImageField(
		upload_to='movies/static/movies/images/films/%Y/%m/%d',
		processors=[ResizeToFill(270, 385)],
		format='PNG',
		options={'quality': 60})

	trailer = models.CharField(max_length=500)
	opening_day = models.DateTimeField()
	movie_lenght = models.CharField(max_length=250)
	description = RichTextUploadingField()
	CHOCIE_STATUS = (
		('NR', u'Phim sắp chiếu'),
		('NS', u'Phim đang chiếu '),
		)
	status = models.CharField(max_length=2, choices=CHOCIE_STATUS, default='NR')
	created_at = models.DateField()

	class Meta:
		ordering = ('-created_at',)

	def __unicode__(self):
		return self.name

class FilmCategory(models.Model):
	film = models.ForeignKey(Film, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE) 

class FilmDirector(models.Model):
	film = models.ForeignKey(Film, on_delete=models.CASCADE)
	director = models.ForeignKey(Director, on_delete=models.CASCADE)

class FilmActor(models.Model):
	film = models.ForeignKey(Film, on_delete=models.CASCADE)
	actor = models.ForeignKey(Actor, on_delete=models.CASCADE)

class Showtime(models.Model):
	film = models.ForeignKey(Film, on_delete=models.CASCADE)
	showdate = models.DateField()

class Showtime_Detail(models.Model):
	showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
	time = models.DateTimeField()

class User(models.Model):
	name = models.CharField(max_length=250)
	username= models.CharField(max_length=250)
	birtday = models.DateTimeField()
	email = models.CharField(max_length=250)
	password = models.CharField(max_length=250)
	phone = PhoneNumberField()
	image = models.CharField(max_length=500)
	ROLE = (
		(1, u'Admin'),
		(2, u'Editor'),
		(3, u'User'),
		)
	ACTIVE = (
		(1, u'Active'),
		(2, u'Block'),
		)
	role = models.IntegerField(choices=ROLE, default=3)
	is_active = models.IntegerField(choices=ACTIVE, default=1)
