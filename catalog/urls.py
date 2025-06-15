from django.urls import path

from . import views

app_name = "catalog"

urlpatterns = [
    path("contacts/", views.contacts, name="contacts"),
    path("product_detail/<int:product_id>", views.product_detail, name="product_detail"),
    path("main/", views.product_list_home, name="product_list_home"),
]
