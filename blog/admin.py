from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content", "is_published", "views_counter")
    list_filter = ("title", "is_published")
    search_fields = ("title",)
