from django.urls import path

from catalog.views import (ContactTemplateView, ProductCreateView, ProductDeleteView, ProductDetailView,
                           ProductListView, ProductUpdateView)

app_name = "catalog"

urlpatterns = [
    path("contacts/", ContactTemplateView.as_view(), name="contacts"),
    path("products/<int:pk>/detail/", ProductDetailView.as_view(), name="product_detail"),
    path("main/", ProductListView.as_view(), name="product_list_home"),
    path("product/create/", ProductCreateView.as_view(), name="product_create"),
    path("product/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
]
