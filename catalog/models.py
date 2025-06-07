from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name="Наименование категории")
    category_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["category_name"]


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name="Наименование товара")
    product_description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="photos/", verbose_name="Фотография товара")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    product_price = models.IntegerField(help_text="Цена продукта")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.category} {self.product_name} {self.product_price} {self.created_at}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["product_name"]
