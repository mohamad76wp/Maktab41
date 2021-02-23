from django.contrib import admin
from .models import User, Email,Address
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as UserBaseAdmin
# Register your models here.


class AddressAdmin(admin.TabularInline):
    """
    Tabular inline admin for manage Address model, then add to User admin
    """
    model = Address
    verbose_name = _("Address")
    verbose_name_plural = _("Addresses")
    extra = 0


class EmailAdmin(admin.TabularInline):
    """
    Tabular inline admin for manage Email model, then add to User admin
    """
    model = Email
    verbose_name = _("Email")
    verbose_name_plural = _("Emails")
    extra = 0


@admin.register(User)
class UserAdmin(UserBaseAdmin):
    """
    User admin, which to use for mange User data
    """
    ordering = ("email",)
    list_display = ("email", "is_staff", "is_admin", "is_active")
    list_per_page = 10
    list_display_links = ("email",)
    search_fields = ("email",)
    add_fieldsets = (
        (None, {"fields": ("email", "fullname",
                           "mobile", "image", "password1", "password2")}),
    )
    fieldsets = ((None, {"fields": ("email", "fullname","password")}), ("Personal Option", {
                 "fields": ("image",)}), ("Status", {"fields": ("is_staff", "is_active")}))
    inlines = (
        EmailAdmin,
        AddressAdmin,
    )

