from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    slug = models.SlugField(_("Slug"), unique=True, db_index=True)
    parent = models.ForeignKey("self", verbose_name=(
        _("Parent")), related_name="children", related_query_name="children", on_delete=models.SET_NULL, null=True,
                               blank=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ["title"]

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(_("Title"), max_length=128)
    # unique means should'nt be repeated date in this field
    slug = models.SlugField(_("slug"), db_index=True, unique=True)
    content = models.TextField(_("Content"))
    # auto_now_add  when object create will submit
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    # auto_now when object updated will modified
    update_at = models.DateTimeField(_("Update at"), auto_now=True)
    publish_at = models.DateTimeField(
        _("Publish at"), db_index=True)
    draft = models.BooleanField(_("Draft"), default=True, db_index=True)
    image = models.ImageField(_("Image"), upload_to="post/images")
    category = models.ForeignKey(Category, verbose_name=(
        _("category")), related_name="category", related_query_name="category", null=True, blank=True,
                                 on_delete=models.SET_NULL)
    author = models.ForeignKey(User, verbose_name=(
        _("Author")), related_name="posts", related_query_name="posts", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ["title"]

    def __str__(self):
        return self.title


class Post_setting(models.Model):
    post = models.OneToOneField(
        "Post", verbose_name=_("Post"), on_delete=models.CASCADE)
    comment = models.BooleanField(_("Published"), default=True)
    public = models.BooleanField(_("Public"), default=True)
    author = models.BooleanField(_("Author"), default=True)
    allow_discussion = models.BooleanField(_("Allow discussion"), default=True)

    class Meta:
        verbose_name = _("Post_setting")
        verbose_name_plural = _("Post_settings")

    def __str__(self):
        return str(self.post)


class Comment_like(models.Model):
    author = models.ForeignKey(User, verbose_name=(
        _("Author")), on_delete=models.CASCADE)
    comment = models.ForeignKey("blog.Comment", verbose_name=(
        _("Comment")), related_name="comment_like", related_query_name="comment_like", on_delete=models.CASCADE)
    condition = models.BooleanField(_("Condition"), default=True)
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)

    class Meta:
        verbose_name = _("Comment_like")
        verbose_name_plural = _("Comment_likes")

    def __str__(self):
        status = str(self.condition)
        if status == True:
            return "Like"
        else:
            return "Dislike"


class Comment(models.Model):
    post = models.ForeignKey(Post, verbose_name=(
        _("Post")), related_name="comment", related_query_name="comment", on_delete=models.CASCADE)
    content = models.TextField(_("Content"))
    author = models.ForeignKey(User, verbose_name=(
        _("Author")), on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(_("confirm"), default=True)
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        ordering = ["create_at"]

    def __str__(self):
        return self.content

    # @property
    # def like_count(self):
    #     query_set = Comment_like.ojects.filter(comment=self)
    #     likes = query_set.filter(condition=True)

    #     return likes.count()

    # @property
    # def dislike_count(self):
    #     query_set = Comment_like.objects.filter(comment=self)
    #     dislikes = query_set.filter(condition=False)

    # return dislikes.count()
