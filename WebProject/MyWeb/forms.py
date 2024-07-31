# MyWeb/forms.py
#from django import forms
#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User

#class RegisterForm(UserCreationForm):
    #email = forms.EmailField(required=True)

    #class Meta:
        #model = User
        #fields = ['username', 'email', 'password1', 'password2']
# THESE LINES ARE THE OLD AND WORKING, INCASE SOMETHING GOES WRONG WITH THE NEW

# MyWeb/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
