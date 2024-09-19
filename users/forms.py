from users.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms 

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    mobile = forms.CharField(max_length = 15)

    def clean(self):
        cleaned_data = super(UserRegistrationForm, self).clean()
        return cleaned_data
    class Meta:
        model = User
        fields = ['username', 'mobile', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
    

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class Login(forms.Form):
    username = forms.CharField(label='username', max_length=50)
    mobile = forms.CharField(label='mobile', max_length=15)
    password = forms.CharField(label='password', max_length=100, widget=forms.PasswordInput())


