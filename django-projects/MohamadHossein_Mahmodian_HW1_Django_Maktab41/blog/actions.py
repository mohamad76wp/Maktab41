from django.contrib import messages
from django.utils.translation import ngettext

def make_draft(modeladmin,request, queryset):
    drafted = queryset.update(draft = True)
    modeladmin.message_user_draft=(request,ngettext(f"{drafted} post was successfully marked as drafted",f"{drafted} posts were successfully marked as drafted.",drafted),messages.SUCCESS)
make_draft.short_description = "Draft"

def make_publish(modeladmin,request, queryset):
    published = queryset.update(draft = False)
    modeladmin.message_user(request,ngettext(f"{published} post was successfully marked as published.",f"{published} posts were successfully marked as published.",published) ,messages.SUCCESS)
make_publish.short_description = "Publish"

