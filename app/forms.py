from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from cloudinary.forms import CloudinaryFileField

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'email', 'photo', 'bio']

class NeighbourHoodForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        fields = ['name','location','admin','photo','description','health_toll','police_toll']


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name','email','description','neighbourhood','user']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','description','image','hood','user']