# in file baraye validate field ha dar method haye clean toye file "forms.py" estefade mishe
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
User = get_user_model()

def validate_confirm_password(password, confirm_password):
    if password != confirm_password:
        raise ValidationError(_('Password is not match'), code='invalid')


def validate_username(username):
    if len(username) < 5:
        raise ValidationError(_('username is less than 5 character'), code='invalid')
    try:
        User.objects.get(username=username)
        raise ValidationError(
            _(f'"{username}" already exist'), code='invalid')
    except User.DoesNotExist:
        pass