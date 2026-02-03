from django import forms
from django.contrib.auth import get_user_model

from .models import Profile

User = get_user_model()


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image', 'full_name', 'phone', 'about', 'location', 'website')
        widgets = {
            'about': forms.Textarea(attrs={'rows': 4}),
        }
