from django.conf.urls import url,include

from . import views

app_name = 'movies'

urlpatterns = [
	url(r'^$', views.base, name='base'),
	url(r'^home/$', views.home, name='home'),
	url(r'^login/$', views.login, name='login'),
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^resgiter/$', views.register, name='register'),
	url(r'^film/$', views.film, name='film'),
	url(r'^film_detail/$', views.film_detail, name='film_detail'),
]