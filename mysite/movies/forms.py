from django import forms
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class UserRegisterForm(forms.Form):
	name = forms.CharField(
		max_length=32, 
		required=True,
		label= 'Họ và tên',
		)
	email = forms.EmailField(
		max_length=254,
		required = True,
		label = 'Email'
		) 
	birthday = forms.DateFiled()
	phone = forms.PhoneNumberField()
	password = forms.CharField(
		required = True,
		label = 'Mật khẩu',
		max_length = 32,
		widget = forms.PasswordInput()
		)