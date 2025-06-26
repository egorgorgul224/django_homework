from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from blog.models import Article


# Create your views here.
class ArticleListView(ListView):
    model = Article

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ArticleCreateView(CreateView):
    model = Article
    fields = ("title", "content", "image", "is_published")
    success_url = reverse_lazy("blog:article_list_home")


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ("title", "content", "image", "is_published")
    success_url = reverse_lazy("blog:article_list_home")

    def get_success_url(self):
        return reverse("blog:article_detail", args=[self.kwargs.get("pk")])


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy("blog:article_list_home")
