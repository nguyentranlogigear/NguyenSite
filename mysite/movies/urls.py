from django.conf.urls import url,include
# from django.contrib.auth.views import login
# from django.contrib.auth.views import logout
# from django.contrib.auth.views import logout_then_login
from django.contrib.auth.views import password_change
from django.contrib.auth.views import password_change_done


from . import views

app_name = 'movies'

urlpatterns = [
	
	url(r'^login/$', views.user_login, name='login'),
	url(r'^password-change/$', password_change, name='password_change'),
	url(r'^password-change/done/$', password_change_done, name='password_change_done'),
	url(r'^logout/$', views.logout, name='logout'),
	
	# Home
	url(r'^$', views.home, name='home'),

	url(r'^register/$', views.register, name='register'),
	url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),

	url(r'^uncoming_movies/$', views.uncoming_movies, name='uncoming_movies'),
	url(r'^film_showing/$', views.film_showing, name='film_showing'),
	url(r'^film_detail/(?P<id>[0-9]+)/$', views.film_detail, name='film_detail'),

	url(r'^promotion_detail/(?P<id>[0-9]+)/$', views.promotion_detail, name='promotion_detail'),


]