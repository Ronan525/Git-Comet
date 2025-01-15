from django import forms
from allauth.account.forms import LoginForm

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update({'class': 'form-control custom-input', 'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update({'class': 'form-control custom-input', 'placeholder': 'Password'})
        self.fields['remember'].widget.attrs.update({'class': 'form-check-input custom-check'})