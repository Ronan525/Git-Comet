from django import forms
from allauth.account.forms import LoginForm, SignupForm
from .models import UserProfile

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update({'class': 'form-control custom-input', 'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update({'class': 'form-control custom-input', 'placeholder': 'Password'})
        self.fields['remember'].widget.attrs.update({'class': 'form-check-input custom-check'})

from allauth.account.forms import SignupForm

class CustomSignUpForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control custom-input', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'class': 'form-control custom-input', 'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control custom-input', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control custom-input', 'placeholder': 'Confirm Password'})

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture']