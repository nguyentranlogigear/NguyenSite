# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit import ImageSpec, register
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
from django.core.exceptions import ValidationError


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
	created_at = models.DateTimeField()
	ACTIVE = (
		(1, u'Active'),
		(2, u'Block'),
		)
	is_active = models.IntegerField(choices=ACTIVE, default=1)

	def __unicode__(self):
		return self.name

	def clean(self):
		if self.start_date > self.end_date:
			raise ValidationError('Start date cannot precede end date')
	def save(self, *args, **kwargs):
		super(Promotion, self).save(*args, **kwargs)


class Film(models.Model):
	category = models.ManyToManyField(Category, related_name='category')
	director = models.ManyToManyField(Director, related_name='director')
	actor = models.ManyToManyField(Actor, related_name='actor')
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

class Showtime(models.Model):
	film = models.ForeignKey(Film, on_delete=models.CASCADE)
	showdate = models.DateField()

	def __unicode__(self):
		return u"{0} [{1}]".format(self.film, self.showdate)

class Showtime_Detail(models.Model):
	showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
	time = models.TimeField()

	def __unicode__(self):
		return u"{0} [{1}]".format(self.showtime, self.time)

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	birtday = models.DateField(null=True, blank=True)
	phone = PhoneNumberField(blank=True)
	image = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
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

