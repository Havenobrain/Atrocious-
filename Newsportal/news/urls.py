from django.urls import path

from .views import PostList, PostDetail, NewsCreate, ArticleCreate, NewsUpdate, ArticleUpdate, NewsDelete, ArticleDelete

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:id>', PostDetail.as_view(), name='post_detail'),
    path('create/news/', NewsCreate.as_view(), name='create_news'),
    path('create/article/', ArticleCreate.as_view(), name='create_article'),
    path('<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
    path('<int:pk>/update/', ArticleUpdate.as_view(), name='article_update'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),



]