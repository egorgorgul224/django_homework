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

        self.fields["product_name"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите название продукта"
        })

        self.fields["product_description"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите описание продукта"
        })

        self.fields["category"].widget.attrs.update({
            "class": "form-select",
        })

        self.fields["product_price"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите стоимость товара"
        })

    def clean_price(self):
        product_price = self.cleaned_data.get("product_price")
        if product_price < 0:
            raise ValidationError("Стоимость не может быть отрицательной")
        return product_price

    # def clean_name(self):
    #
    #     name = self.cleaned_data.get("product_name").lower().spilt()
    #     for elem in name:
    #         if elem in BAN_WORDS:
    #             raise ValidationError("Название товара содержит недопустимое(ые) слово(а)")
    #     return name
    #
    # def clean_description(self):
    #     description = self.cleaned_data.get("product_description").lower().split()
    #     for word in description:
    #         if word in BAN_WORDS:
    #             raise ValidationError("Описание содержит недопустимое(ые) слово(а)")
    #     return description