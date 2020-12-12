from django.contrib import admin

from .models import Post, Post_setting, Category, Comment, Comment_like, User

from .actions import make_publish , make_draft
# Register your models here.


class ChildrenItemInline(admin.TabularInline):
    model = Category
    fields = [
        "slug",
    ]
    extra = 1
    show_change_link = True


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    # show the columns of the admin table
    list_display = ("title", "slug", "parent",)
    search_fields = ("title", "slug",)  # set fields that search crwal on them
    list_filter = ("parent",)  # set filds for the filter
    inlines = [
        ChildrenItemInline,
    ]


class PostSettingAdminInline (admin.TabularInline):
    model = Post_setting
    fields = [
        "public",
        "author",
        "allow_discussion"
    ]

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ("title", "category", "author", "draft",
                    "publish_at", "create_at", "update_at",)
    list_filter = ("draft", "author",)
    search_fields = ("title",)
    date_hierarchy = ("publish_at")
    inlines = [
        PostSettingAdminInline,
    ]
    actions = [make_publish,make_draft]



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("is_confirmed", "post", "author",)
    list_filter = ("is_confirmed",)
    search_fields = ("content",)
    date_hierarchy = ("create_at")


@admin.register(Comment_like)
class CommentLikeAdmin(admin.ModelAdmin):
    list_display = ("comment", "author", "__str__",)
    list_filter = ("author", "condition",)
    search_fields = ("comment",)
