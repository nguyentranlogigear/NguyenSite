from django.conf.urls import url,include
# from django.contrib.auth.views import login
# from django.contrib.auth.views import logout
# from django.contrib.auth.views import logout_then_login

from . import views

app_name = 'movies'

urlpatterns = [
	
	url(r'^login/$', views.user_login, name='login'),
	# url(r'^login/$', login, name='login'),
	url(r'^logout/$', views.logout, name='logout'),
	
	# Home
	url(r'^$', views.home, name='home'),

	url(r'^register/$', views.register, name='register'),
	url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),

	url(r'^film/$', views.film, name='film'),
	url(r'^film_detail/$', views.film_detail, name='film_detail'),
]