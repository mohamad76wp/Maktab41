from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
User = get_user_model()


class Category(models.Model):
    name = models.TextField(_("Name"))
    product = models.ForeignKey("products.Product", verbose_name=_(
        "product"), on_delete=models.SET_NULL, null=True,related_name="CategroyForHome",related_query_name="CategroyForHome")

    class Meta:
        verbose_name = _("Basket")
        verbose_name_plural = _("Baskets")

    def __str__(self):
        return self.name
