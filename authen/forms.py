from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, help_text='Required. 100 charaters of fewer.')
    email = forms.EmailField()
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('full_name','email')
