from django import forms
from django.utils.translation import ugettext_lazy as _


class UserRegistrationForm(forms.Form):
    username = forms.CharField(label=_('Username'), max_length=150)
    email = forms.EmailField(label=_('Email'), required=True, help_text=_(
        'Valid email for reset password'))
    password = forms.CharField(
        label=_('Password'), widget=forms.PasswordInput(), required=True)
    confirm_password = forms.CharField(
        label=_('Repeat Password'), widget=forms.PasswordInput(), required=True)
    first_name = forms.CharField(label=_('First name'))
    last_name = forms.CharField(label=_('Last name'))