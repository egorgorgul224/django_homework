from django.urls import path

from blog.apps import BlogConfig
from blog.views import ArticleCreateView, ArticleDeleteView, ArticleDetailView, ArticleListView, ArticleUpdateView

app_name = BlogConfig.name

urlpatterns = [
    path("main/", ArticleListView.as_view(), name="article_list_home"),
    path("articles/<int:pk>/detail/", ArticleDetailView.as_view(), name="article_detail"),
    path("article/create/", ArticleCreateView.as_view(), name="article_create"),
    path("article/<int:pk>/update/", ArticleUpdateView.as_view(), name="article_update"),
    path("article/<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
]
