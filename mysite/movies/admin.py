# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Category, Director, Actor, Promotion, Film, FilmCategory, FilmDirector, FilmActor, Showtime, Showtime_Detail, User

class ShowtimeDatailInline(admin.StackedInline):
	"""docstring for ShowtimeDatailInline"""
	model = Showtime_Detail
	extra = 10

class ShowtimeAdmin(admin.ModelAdmin):
	filedsets = [
		(None, {'fields': ['film']}),
		('Show Date', {'fields':['showdate'], 'classes':['collapse']}),
	]
	inlines = [ShowtimeDatailInline]
		

admin.site.register(Category)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Promotion)
admin.site.register(Film)
admin.site.register(FilmCategory)
admin.site.register(FilmDirector)
admin.site.register(FilmActor)
admin.site.register(Showtime,ShowtimeAdmin )
admin.site.register(Showtime_Detail)
admin.site.register(User)