from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
User = get_user_model()


class Category(models.Model):
    name = models.CharField(_("Name"),max_length=256)
    product = models.ForeignKey("products.Product", verbose_name=_(
        "product"), on_delete=models.SET_NULL, null=True, related_name="CategroyForHome", related_query_name="CategroyForHome")

    class Meta:
        verbose_name = _("Basket")
        verbose_name_plural = _("Baskets")

    def __str__(self):
        return self.name


class Carousel(models.Model):
    name = models.CharField(_("Name"),max_length=256)
    status = models.BooleanField(_("Status"), default=False)

    class Meta:
        verbose_name = _("Carousel")
        verbose_name_plural = _("Carousels")

    def __str__(self):
        return self.name


def upload_gallery_image(instance, filename):
    return f"carousel_image/{instance.carousel.name}_{filename}"


class Carousel_image(models.Model):
    slide_image = models.ImageField(
        _("Slide Image"), upload_to=upload_gallery_image)

    carousel = models.ForeignKey(Carousel, verbose_name=_(
        "Carousel"), on_delete=models.CASCADE, related_name="slide_images", related_query_name="slide_images")
