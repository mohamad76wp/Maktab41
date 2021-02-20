from django.db import models
from django.utils.translation import ugettext_lazy as _

class Product(models.Model):
    name = models.CharField(_('Name'), max_length=64)
    brand = models.ForeignKey("Brand", verbose_name=_('Brand'), on_delete=models.SET_NULL, null=True,
                              related_name='Brand',
                              related_query_name='Brand')
    category = models.ForeignKey("Category", verbose_name=_('Category'), on_delete=models.SET_NULL, null=True,
                                 related_name='product', related_query_name='product')
    slug = models.SlugField(_('Slug'), )
    image = models.ImageField(_('Image'), upload_to='media/product_image')
    details = models.CharField(_('Details'), max_length=32)
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now_add=True)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name


class ShopProduct(models.Model):
    shop = models.ForeignKey('accounts.Shop', verbose_name=_('Shop'), on_delete=models.SET_NULL, null=True,
                             related_name='shop',
                             related_query_name='shop')
    product = models.ForeignKey(Product, verbose_name=_('Product'), on_delete=models.SET_NULL, null=True,
                                 related_name='product', related_query_name='product')
    price = models.IntegerField(_('Price'))
    quantity = models.IntegerField(_('Quantity'))
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now_add=True)

    class Meta:
        verbose_name = _("ShopProduct")
        verbose_name_plural = _("ShopProducts")


class Brand(models.Model):
    name = models.CharField(_('Name'), max_length=64)
    details = models.CharField(_('Details'), max_length=64)
    image = models.ImageField(_('Image'), upload_to='media/brand_image')
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now_add=True)

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

    def __str__(self):
        return self.name


class Category(models.Model):
    category = models.ForeignKey('Category', verbose_name=_('Category'), on_delete=models.SET_NULL, null=True,
                                 related_name='child', related_query_name='child')
    slug = models.SlugField(_('Slug'), )
    name = models.CharField(_('Name'), max_length=32)
    details = models.CharField(_('Details'), max_length=32)
    image = models.ImageField(_('Image'), upload_to='media/category_image')
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now_add=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name




class Discount(models.Model):
    title = models.CharField(_('Title'), max_length=128)
    product = models.ForeignKey("Product", verbose_name=_("product"), related_name='Discount_product',
                                related_query_name='Discount_product', on_delete=models.SET_NULL, null=True)
    value = models.IntegerField(_('Value'))
    is_percent = models.BooleanField(_('Is Percent'), default=True)
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now_add=True)
    expire_at = models.DateTimeField(_("Create at"), auto_now_add=True)

    class Meta:
        verbose_name = _("Discount")
        verbose_name_plural = _("Discounts")

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField(_("Content"))
    product = models.ForeignKey("Product", verbose_name=_("Product"), related_name='comment',
                                related_query_name='comment', on_delete=models.SET_NULL, null=True)
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)
    user = models.ForeignKey('accounts.User', verbose_name=_(
        "User"), on_delete=models.SET_NULL, null=True)
    is_confirmed = models.BooleanField(_("confirm"), default=True)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        ordering = ['-create_at']

    def __str__(self):
        return self.post.title


class ProductMeta(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("Product"), related_name='productMeta',
                                related_query_name='productMeta', on_delete=models.SET_NULL, null=True)
    label = models.CharField(_('Label'), max_length=32)
    value = models.IntegerField(_('Value'), )

    class Meta:
        verbose_name = _("ProductMeta")
        verbose_name_plural = _("ProductMetas")

    def __str__(self):
        return self.post.label


class Like(models.Model):
    user = models.ForeignKey('accounts.User', verbose_name=_('User'), on_delete=models.SET_NULL, null=True,
                             related_name='like',
                             related_query_name='like')
    product = models.ForeignKey(Product, verbose_name=_('Product'), on_delete=models.SET_NULL, null=True,
                                related_name='like',
                                related_query_name='like')
