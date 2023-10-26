from django.contrib import admin

from blogs.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
