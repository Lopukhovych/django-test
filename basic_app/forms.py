from django import forms
from basic_app.models import UserInfoModel
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):

    class Meta:
        model = UserInfoModel
        fields = ('github_link', 'profile_pic')

