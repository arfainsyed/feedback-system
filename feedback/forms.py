from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Feedback

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['created_for', 'strengths', 'areas_to_improve', 'sentiment']
        widgets = {
            'created_for': forms.Select(attrs={'class': 'form-select'}),
            'strengths': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
            'areas_to_improve': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
            'sentiment': forms.Select(attrs={'class': 'form-select'}),
        }

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2'] 
