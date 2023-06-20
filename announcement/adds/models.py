from datetime import datetime

from django.db import models
from accounts.models import CustomUser
from ckeditor_uploader.fields import RichTextUploadingField


CATEGORY = [
    ('TK', 'Танки'),  # tanks
    ('HL', 'Хилы'), # heal
    ('DD', 'ДД'), # damage dealler
    ('TM', 'Торговцы'),  # tradesman
    ('GM', 'Гилдмастеры'),
    ('QG', 'Квестгиверы'),
    ('BM', 'Кузнецы'),  # blacksmith
    ('TN', 'Кожевники'),  # tanner
    ('PM', 'Зельевары'),  # potion master
    ('IM', 'Мастера заклинаний')  # incantation master
]


class Advertisement(models.Model):
    title = models.CharField("Заголовок", max_length=100, blank=False)
    text = RichTextUploadingField("Текст")
    category = models.CharField("Категория", max_length=2, choices=CATEGORY)
    date_publication = models.DateTimeField("Дата публикации", default=datetime.now, blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='author')

    def __str__(self):
        return f'{self.title}'


class Reply(models.Model):
    text = models.TextField("Текст")
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='adds', verbose_name="Объявление")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user', verbose_name="Пользователь")
    status = models.BooleanField(default=False)
    date_publication = models.DateTimeField("Дата публикации", default=datetime.now, blank=True)




