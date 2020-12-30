from django.db import models
from django.utils.translation import ugettext_lazy as _


class Basket(models.Model):
    unique = models.CharField(_('UniqueID'), max_length=256)
    Product = models.ForeignKey('products.Product', verbose_name=_('Category'), on_delete=models.CASCADE(),
                                related_name='Basket', related_query_name='Basket', )
    user = models.ForeignKey('accounts.User', verbose_name=_('User'), on_delete=models.CASCADE())
    full_price = models.IntegerField(_('Full price'), )
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    paid_at = models.DateTimeField(_("Paid at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now_add=True)

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

    def __str__(self):
        return self.name


class Order(models.Model):
    pass


class Payment(models.Model):
    pass
