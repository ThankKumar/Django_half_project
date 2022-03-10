from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
 class Meta:
  model = User
  field = ['user_name','first_name','last_name','email']
  