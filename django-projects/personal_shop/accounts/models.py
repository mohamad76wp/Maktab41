from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Create your models here.

class MyUserManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("User must have Email")
        if not username:
            raise ValueError("User must have Username")

        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_staffuser(self,email,username,password=None):
        
        user = self.model(email,username=username,password=password)
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,password=None):
        
        user = self.model(email,username=username,password=password)
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    username = models.CharField(_("Username"), max_length=128,)
    email = models.EmailField(_("Email"), unique=True,
                              db_index=True, max_length=256)
    password = models.CharField(_("Password"), max_length=64)
    mobile = models.CharField(_("Mobile"), max_length=12, unique=True)
    fullname = models.CharField(_("First Name"), max_length=64)
    image = models.ImageField(_("Profile Image"), upload_to="media/profile")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    is_active = models.BooleanField(_("active"), default=True)
    is_staff = models.BooleanField(_("staff"), default=False)
    is_admin = models.BooleanField(_("admin"),default=False)
    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.username


class Email(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.SET_NULL, null=True, related_name="user",
                             related_query_name="user")
    subject = models.CharField(_("Subject"), max_length=64)
    body = models.CharField(_("Body"), max_length=256)

    class Meta:
        verbose_name = _("Email")
        verbose_name_plural = _("Emails")

    def __str__(self):
        return self.subject




class Address(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.SET_NULL, null=True, related_name="address",
                             related_query_name="address")
    city = models.CharField(_("City"), max_length=32)
    street = models.CharField(_("Street"), max_length=32)
    alley = models.CharField(_("Alley"), max_length=32)
    zip_code = models.CharField(_("ZipCode"), max_length=10)

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Address")
