from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class UserRegister(froms.Form):
    user_name = froms.CharField(_("user name"), max_length=50)
    user_email = froms.EmailField(label=_("Email"),)

