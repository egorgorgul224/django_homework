from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

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
