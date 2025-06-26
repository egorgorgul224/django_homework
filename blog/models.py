from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок статьи")
    content = models.TextField(null=True, blank=True, verbose_name="Содержимое статьи")
    image = models.ImageField(upload_to="articles_photo/", verbose_name="Изображение", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    views_counter = models.PositiveIntegerField(verbose_name="Счетчик просмотров", default=0)

    def __str__(self):
        return f"{self.title} {self.content} {self.created_at} {self.views_counter}"

    class Meta:
        verbose_name = "статья"
        verbose_name_plural = "статьи"
        ordering = ["title"]
