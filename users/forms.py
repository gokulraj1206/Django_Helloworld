from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from .models import Profile
from .models import CustomUser

class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField()
    
    class Meta:
        model = CustomUser
        fields = ['username','email','password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False
    class Meta:
        model = CustomUser
        fields = ['username','email','image']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False
    class Meta:
        model = CustomUser
        fields = ("username", "email","image",)

class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False
    class Meta:
        model = CustomUser
        fields = ['username', 'email','image']