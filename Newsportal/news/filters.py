

from django.forms import DateTimeInput
from django_filters import FilterSet, ModelChoiceFilter, DateTimeFilter
from .models import Post, Category

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):
    dateCreation = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
            ),
        )

    category = ModelChoiceFilter(
        field_name = 'postCategory',
        queryset = Category.objects.all(),
        label = 'Категория',
        #conjoined= True,
    )



    class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
       model = Post
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
       fields = {
           # поиск по названию
           'title': ['icontains'] ,
           # количество товаров должно быть больше или равно
           #'quantity': ['gt'],
           #'dateCreation': ['lt']  # цена должна быть меньше или равна указанной
               #'gt',  # цена должна быть больше или равна указанной

        }