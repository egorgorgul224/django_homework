from django.urls import path

from catalog.views import ProductListView, ProductDetailView, ContactTemplateView

app_name = "catalog"

urlpatterns = [
    path("contacts/", ContactTemplateView.as_view(), name="contacts"),
    path("products/<int:pk>/detail/", ProductDetailView.as_view(), name="product_detail"),
    path("main/", ProductListView.as_view(), name="product_list_home"),
]
