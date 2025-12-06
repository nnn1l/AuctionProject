from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from pydantic.v1 import ValidationError

from .models import CustomUser

class CustomUserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Email')
    avatar = forms.ImageField(label='Avatar', required=False)
    biography = forms.CharField(widget=forms.Textarea, label='Biography', required=False)

    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    verify_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'avatar', 'email', 'biography']

    def clean_verify_password(self):
        password = self.cleaned_data.get('password')
        verify_password = self.cleaned_data.get('verify_password')

        if verify_password != password:
            raise forms.ValidationError('Password dont match!')
        return verify_password


    def save(self, commit=True):
        user = super().save(commit=False)

        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.biography = self.cleaned_data.get('biography')

        if 'avatar' in self.cleaned_data:
            user.avatar = self.cleaned_data['avatar']

        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'avatar', 'email', 'biography']

