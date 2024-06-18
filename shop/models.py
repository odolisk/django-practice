from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Категория',
        help_text='Введите название категории'
        )
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='Создано',
        help_text='Дата и время создания'
        )

    class Meta:
        verbose_name = 'Категория курсов'
        verbose_name_plural = 'Категории курсов'
        ordering = ('title',)

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Курс',
        help_text='Введите название курса'
        )
    price = models.FloatField(
        verbose_name='Цена',
        help_text='Введите цену курса',
        validators=[
            MinValueValidator(0.01)
        ]
    )
    students_qty = models.PositiveIntegerField(
        verbose_name='Количество учащихся',
        help_text='Введите количество стедентов на курсе',
        default=0,
    )
    comments_qty = models.PositiveIntegerField(
        verbose_name='Количество комментариев',
        help_text='Введите количество комментариев для курса',
        default=0
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='course_category',
        verbose_name='Категория',
        help_text='Выберите категорию курса'
        )
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='Создано',
        help_text='Дата и время создания'
        )

    class Meta:
        verbose_name = 'Учебный курс'
        verbose_name_plural = 'Учебные курсы'
        ordering = ('pk',)

    def __str__(self):
        return f'{self.title}'
