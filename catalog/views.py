from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.models import Product


# Create your views here.
class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ContactTemplateView(TemplateView):
    template_name = "catalog/contacts.html"

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            name = request.POST.get("name")
            phone = request.POST.get("phone")
            message = request.POST.get("message")
            return HttpResponse(f"Спасибо, {name}! Сообщение получено.")
        return render(request, "catalog/contacts.html")


class ProductCreateView(CreateView):
    model = Product
    fields = ("product_name", "product_description", "image", "category", "product_price")
    success_url = reverse_lazy("catalog:product_list_home")


class ProductUpdateView(UpdateView):
    model = Product
    fields = ("product_name", "product_description", "image", "category", "product_price")
    success_url = reverse_lazy("catalog:product_list_home")

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list_home")