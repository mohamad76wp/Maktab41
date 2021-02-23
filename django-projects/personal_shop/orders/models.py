from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
User = get_user_model()


class Basket(models.Model):
    user = models.ForeignKey(User, verbose_name=_('User'), on_delete=models.SET_NULL, null=True,
                             related_name='basket', related_query_name='basket')

    class Meta:
        verbose_name = _("Basket")
        verbose_name_plural = _("Baskets")


class BasketItem(models.Model):
    basket = models.ForeignKey('Basket', verbose_name=_('Basket'), on_delete=models.SET_NULL, null=True,
                               related_name='basket_item', related_query_name='basket_item', )
    shop_product = models.ForeignKey('products.ShopProduct', verbose_name=_('shop_product'), on_delete=models.SET_NULL,
                                     null=True, related_name='basket_item', related_query_name='basket_item', )

    class Meta:
        verbose_name = _("BasketItem")
        verbose_name_plural = _("BasketItems")


class Order(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.SET_NULL, null=True,
                             related_name='order', related_query_name='order')
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now_add=True)
    description = models.CharField(_('Description'), max_length=128)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name=_("order"), on_delete=models.SET_NULL, null=True,
                              related_name='Order_Item',
                              related_query_name='Order_Item')
    shop_product = models.ForeignKey('products.ShopProduct', verbose_name=_("shop_product"), on_delete=models.SET_NULL,
                                     null=True, related_name='Order_Item', related_query_name='Order_Item')
    count = models.IntegerField(_('Number of bought item'))
    price = models.IntegerField(_('Price'))


class Payment(models.Model):
    order = models.ForeignKey(Order, verbose_name=_("order"), on_delete=models.SET_NULL, null=True,
                              related_name='payment',
                              related_query_name='payment')
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.SET_NULL, null=True,
                             related_name='payment', related_query_name='payment')
    amount = models.CharField(_('amount'), max_length=16)

    status = models.BooleanField(
        verbose_name=_("Payment Status"), default=False)
