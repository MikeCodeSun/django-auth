from django.contrib.auth.forms import AuthenticationForm 
from django.forms import TextInput, PasswordInput,CharField


class LoginForm(AuthenticationForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    
  username = CharField(widget=TextInput(
    attrs={'class': 'form-control ', 'placeholder': 'username', 'id': 'username'}
  ))
  password = CharField(widget=PasswordInput(
    attrs={'class': 'form-control', 'placeholder': 'password', 'id': 'password'}
  ))
  
  