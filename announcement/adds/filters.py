import django_filters.widgets
from django_filters import FilterSet, CharFilter, DateFromToRangeFilter, DateFilter, ModelChoiceFilter
from django_filters.widgets import DateRangeWidget

from .models import Reply, Advertisement

CATEGORY = [
    ('TK', 'Танки'),  # tanks
    ('HL', 'Хилы'), # heal
    ('DD', 'ДД'),
    ('TM', 'Торговцы'),  # tradesman
    ('GM', 'Гилдмастеры'),
    ('QG', 'Квестгиверы'),
    ('BM', 'Кузнецы'),  # blacksmith
    ('TN', 'Кожевники'),  # tanner
    ('PM', 'Зельевары'),  # potion master
    ('IM', 'Мастера заклинаний')  # incantation master
]


class ReplyFilter(FilterSet):
    user = CharFilter(
            field_name='user__username',
            lookup_expr='icontains',
            label='Пользователь'
        )
    date_publication = DateFromToRangeFilter(widget=DateRangeWidget(attrs={'placeholder': 'ГГГГ.ММ.ДД'}), label='За период')

    class Meta:
        model = Reply
        fields = ['advertisement']
