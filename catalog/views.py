from django.http import HttpResponse
from django.shortcuts import render
from catalog.models import Category, Product


# Create your views here.
def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо, {name}! Сообщение получено.")
    return render(request, "catalog/contacts.html")


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        "product": product,
    }
    return render(request, "catalog/product_detail.html", context=context)


def product_list_home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/home.html', context)
