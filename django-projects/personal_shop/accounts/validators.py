from django.forms import ValidationError
from django.contrib.auth import get_user_model() as User


def password_validator(password1,password2):
    if len(password1)<8:
        raise ValidationError("Password is too short (minimum 8)")
    if password1 != password2:
        raise ValidationError("Passwords are not match")


def email_validator(email):
    try:
        email = User.objects.get(email=email)
        raise ValidationError(f"`{email}` is alrady exist.")
    except email.DoseNotExist:
        pass

def username_validator(username):

    try:
        user = user.objects.get(username=username)
        raise ValidationError(f"`{username}` is alrady exist.")
    except user.DoseNotExist:
        pass        
    