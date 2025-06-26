from django import forms
from .models import Product
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["product_name", "product_description", "image", "category", "product_price",]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["product_name"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите название продукта"
        })

        self.fields["product_description"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите описание продукта"
        })

        self.fields["category"].widget.attrs.update({
            "class": "form-check",
        })

        self.fields["product_price"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите стоимость товара"
        })

    # def clean_name(self):
    #     ban_words = ["казино", "биржа", "обман", "криптовалюта", "дешево", "полиция", "крипта", "бесплатно", "радар"]
    #     name = self.cleaned_data.get("product_name").lower().spilt()
    #     for elem in name:
    #         if elem in ban_words:
    #             raise ValidationError("Название товара содержит недопустимое(ые) слово(а)")
    #     return name
    #
    # def clean_description(self):
    #     ban_words = ["казино", "биржа", "обман", "криптовалюта", "дешево", "полиция", "крипта", "бесплатно", "радар"]
    #     description = self.cleaned_data.get("product_description")
    #     for word in description.lower().split():
    #         if word in ban_words:
    #             raise ValidationError("Описание содержит недопустимое(ые) слово(а)")
    #     return description
    #
    # def clean_price(self):
    #     price = self.cleaned_data.get("price")
    #     if price < 0:
    #         raise ValidationError("Стоимость не может быть отрицательной")
    #     return price