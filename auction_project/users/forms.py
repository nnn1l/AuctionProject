from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Email')
    avatar = forms.ImageField(label='Avatar', required=False)
    biography = forms.CharField(widget=forms.Textarea, label='Biography', required=False)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'avatar', 'email', 'biography']

    def save(self, commit=True):
        user = super().save(commit=False)

        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'avatar', 'email', 'biography']

