# Generated by Django 5.0.6 on 2024-06-15 12:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_category_options_alter_course_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='comments_qty',
            field=models.PositiveIntegerField(help_text='Введите количество комментариев для курса', verbose_name='Количество комментариев'),
        ),
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.FloatField(help_text='Введите цену курса', validators=[django.core.validators.MinValueValidator(0.01)], verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='course',
            name='students_qty',
            field=models.PositiveIntegerField(help_text='Введите количество стедентов на курсе', verbose_name='Количество учащихся'),
        ),
    ]
