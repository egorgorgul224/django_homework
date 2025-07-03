from django import forms
from django.core.exceptions import ValidationError

from .models import Product

BAN_WORDS = ["казино", "биржа", "обман", "криптовалюта", "дешево", "полиция", "крипта", "бесплатно", "радар"]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["product_name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите название продукта"}
        )

        self.fields["product_description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание продукта"}
        )

        self.fields["category"].widget.attrs.update(
            {
                "class": "form-select",
            }
        )

        self.fields["product_price"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите стоимость товара"}
        )

    def clean(self):
        cleaned_data = super().clean()
        name = self.cleaned_data.get("product_name")
        description = self.cleaned_data.get("product_description")
        for elem in name.lower().split():
            if elem in BAN_WORDS:
                raise ValidationError(f"Название товара содержит недопустимое слово: {elem}")
        for word in description.lower().split():
            if word in BAN_WORDS:
                raise ValidationError(f"Описание товара содержит недопустимое слово: {word}")

    def clean_product_price(self):
        price = self.cleaned_data.get("product_price")
        if price < 0:
            raise ValidationError("Стоимость не может быть отрицательной")
        return price

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if not image.name.endswith((".jpg", ".jpeg", ".png")):
            raise ValidationError("Неверный формат файла: используйте JPG или PNG")
        if image.size > 5 * 1024 * 1024:
            raise ValidationError("Файл превышает допустимый размер в 5 МБ")
        return image
