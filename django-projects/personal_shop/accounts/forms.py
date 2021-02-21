from django import forms
from validators import password_validator, email_validator , username_validator
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model() as User



class UserRegistrationFrom(forms.ModelForm):
    password1 = froms.CharField(
        label=_("Password"), widget=forms.PasswordInput)
    password2 = forms.CharField(
        lable=_("Confirm Password"), wirget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ("email","username")


    def clean_password(self):

        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        password_validator(password1,password2)
        return password1
    
    def clean_username(self):

        username = self.cleaned_data.get('username')
        username_validator(username)
        return username

    def clean_email(self):

        email = self.cleaned_data.get('email')
        email_validator(email)
        return email