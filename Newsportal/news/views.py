from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .filters import PostFilter
from .forms import PostForm
from django.urls import reverse_lazy

class PostList (ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 1

# Переопределяем функцию получения списка товаров
    def get_queryset(self):
       # Получаем обычный запрос
        queryset = super().get_queryset()
       # Используем наш класс фильтрации.
       # self.request.GET содержит объект QueryDict, который мы рассматривали
       # в этом юните ранее.
       # Сохраняем нашу фильтрацию в объекте класса,
       # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
       # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):

    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    pk_url_kwarg = 'id'

class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_news',)
    # Указываем нашу разработанную форму
    form_class = PostForm
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'news_create.html'

class ArticleCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_article',)
    # Указываем нашу разработанную форму
    form_class = PostForm
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'article_create.html'

class NewsUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_news',)
    form_class = PostForm
    model = Post
    template_name = 'news_create.html'

class ArticleUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_article',)
    form_class = PostForm
    model = Post
    template_name = 'news_create.html'

# Представление удаляющее товар.
class NewsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_news',)
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('post_list')

class ArticleDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_article',)
    model = Post
    template_name = 'article_delete.html'
    success_url = reverse_lazy('post_list')