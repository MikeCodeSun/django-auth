from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.forms import CharField, TextInput, PasswordInput
from django.forms.utils import ErrorList




# Create your views here.
class CustomErrorList(ErrorList):
  def __init__(self, *args, **kwargs) -> None:
    super().__init__(*args,**kwargs)
  

class SignUpForm(UserCreationForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
  username = CharField(widget=TextInput(attrs={'class' : 'form-control', 'placeholder': 'usernmae'}))
  password1 = CharField(widget=PasswordInput(attrs={'class' : 'form-control', 'placeholder': 'password'}))
  password2 = CharField(label='Conform password',widget=PasswordInput(attrs={'class' : 'form-control','placeholder': 'conform password',}))
  
  

class SignUpView(CreateView):
  form_class = SignUpForm
  success_url = reverse_lazy('login')
  template_name = 'registration/signup.html'
  