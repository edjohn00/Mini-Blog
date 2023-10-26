from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class Author(AbstractUser):
    about_me = models.TextField(blank=True, null=True)
    is_alive = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Author")
        default_related_name = "authors"
