from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def validate_confirm_password(password, confirm_password):
    print(password)
    print(confirm_password)
    if password != confirm_password:
        raise ValidationError(_('Password is not match'), code='invalid')


def validate_username(username):
    if len(username) < 5:
        raise ValidationError(_('username is less than 5 character'), code='invalid')
