# Generated by Django 2.2.16 on 2022-08-01 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0010_auto_20220801_0938'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='category',
            name='exclude the re-creation of the сategory',
        ),
        migrations.RemoveConstraint(
            model_name='genre',
            name='exclude the re-creation of the genre',
        ),
        migrations.RemoveConstraint(
            model_name='review',
            name='user can create only one review',
        ),
        migrations.RemoveConstraint(
            model_name='title',
            name='exclude the re-creation of the titles',
        ),
        migrations.AlterField(
            model_name='comment',
            name='review',
            field=models.ForeignKey(help_text='Выберите отзыв', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='reviews.Review', verbose_name='Обзор'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(help_text='Оставьте свой комментарий к отзыву', verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(help_text='Напишите свой отзыв', verbose_name='Текст отзыва'),
        ),
        migrations.AddConstraint(
            model_name='category',
            constraint=models.UniqueConstraint(fields=('name', 'slug'), name='unique_name_slug_category'),
        ),
        migrations.AddConstraint(
            model_name='genre',
            constraint=models.UniqueConstraint(fields=('name', 'slug'), name='unique_name_slug_genre'),
        ),
        migrations.AddConstraint(
            model_name='review',
            constraint=models.UniqueConstraint(fields=('title', 'author'), name='unique_title_author_review'),
        ),
        migrations.AddConstraint(
            model_name='title',
            constraint=models.UniqueConstraint(fields=('name', 'year'), name='unique_name_year_title'),
        ),
    ]
