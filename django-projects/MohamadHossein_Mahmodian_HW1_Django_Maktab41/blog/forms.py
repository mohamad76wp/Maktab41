from blog.validators import validate_confirm_password, validate_username
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model as User
from blog.models import Comment


class UserRegistrationForm(forms.Form):
    username = forms.CharField(label=_('Username'), max_length=150,
                               widget=forms.TextInput(attrs={'class': 'form-control'}), )

    email = forms.EmailField(label=_('Email'), required=True, help_text=_(
        'Valid email for reset password'), widget=forms.EmailInput(attrs={'class': 'form-control'}), )

    password = forms.CharField(
        label=_('Password'), widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)

    confirm_password = forms.CharField(
        label=_('Repeat Password'), widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)

    first_name = forms.CharField(label=_('First name'), widget=forms.TextInput(
        attrs={"class": "form-control"}), )

    last_name = forms.CharField(label=_('Last name'), widget=forms.TextInput(
        attrs={"class": "form-control"}), )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password', None)
        confirm_password = self.cleaned_data.get('confirm_password', None)
        validate_confirm_password(password, confirm_password)

        return confirm_password

    def clean_username(self):
        username = self.cleaned_data.get('username', None)

        validate_username(username)
        return username


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        labels = {'content': ''}
