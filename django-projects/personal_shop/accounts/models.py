from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class User(models.Model):
    password = models.CharField(_('Password'), max_length=64)
    mobile = models.CharField(_('Mobile'), max_length=12, unique=True)
    first_name = models.CharField(_('First Name'), max_length=64)
    last_name = models.CharField(_('Last Name'), max_length=64)
    image = models.ImageField(_('Profile Image'), upload_to='media/profile')

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("User")

    def __str__(self):
        return self.first_name


class Email(models.Model):
    user = models.ForeignKey(User, verbose_name=_('User'), on_delete=models.CASCADE, related_name='email',
                             related_query_name='email')
    subject = models.CharField(_('Subject'), )
    body = models.CharField(_('Body'), )

    class Meta:
        verbose_name = _("Email")
        verbose_name_plural = _("Emails")

    def __str__(self):
        return self.subject


class Shop(models.Model):
    user = models.ForeignKey(User, verbose_name=_('User'), on_delete=models.CASCADE, related_name='shop',
                             related_query_name='shop')
    name = models.CharField(_('Name'), max_length=128)
    slug = models.SlugField(_('Slug'), )
    description = models.CharField(_('Description'), max_length=256)
    logo = models.ImageField(_('Shop logo'), upload_to='media/shop_logo')

    class Meta:
        verbose_name = _("Shop")
        verbose_name_plural = _("Shops")

    def __str__(self):
        return self.name


class Address(models.Model):
    user = models.ForeignKey(User, verbose_name=_('User'), related_name='address', related_query_name='address')
    city = models.CharField(_('City'), max_length=32)
    street = models.CharField(_('Street'), max_length=32)
    alley = models.CharField(_('Alley'), max_length=32)
    zip_code = models.CharField(_('ZipCode'), max_length=10)

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Address")
        ordering = ['-create_at']
