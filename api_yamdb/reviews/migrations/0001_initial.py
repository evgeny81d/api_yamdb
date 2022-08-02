<<<<<<< HEAD
# Generated by Django 2.2.16 on 2022-08-02 17:39
=======
# Generated by Django 2.2.16 on 2022-08-01 09:19
>>>>>>> origin/dev

from django.db import migrations, models
import django.db.models.deletion
import reviews.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Добавьте название категории', max_length=256, verbose_name='Название категории')),
                ('slug', models.SlugField(help_text='Добавьте адрес категории', unique=True, verbose_name='Уникальный адрес категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Оставьте свой комментарий к отзыву', verbose_name='Комментарий')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Комментарий к отзыву',
                'verbose_name_plural': 'Комментарии к отзывам',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Добавьте название жанра', max_length=256, verbose_name='Название жанра')),
                ('slug', models.SlugField(help_text='Добавьте адрес жанра', unique=True, verbose_name='Уникальный адрес жанра')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Напишите свой отзыв', verbose_name='Текст отзыва')),
<<<<<<< HEAD
                ('score', models.PositiveSmallIntegerField(choices=[(None, '---'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default='---', help_text='Дайте оценку произведению от 1 до 10', verbose_name='Оценка')),
=======
                ('score', models.IntegerField(choices=[(None, '---'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default='---', help_text='Дайте оценку произведению от 1 до 10', verbose_name='Оценка')),
>>>>>>> origin/dev
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Добавьте название произведения', max_length=256, verbose_name='Название произведения')),
                ('year', models.PositiveSmallIntegerField(help_text='Добавьте год выпуска произведения', validators=[reviews.models.validate_year], verbose_name='Год выпуска произведения')),
                ('description', models.TextField(blank=True, help_text='Добавьте описание произведения', null=True, verbose_name='Описание произведения')),
                ('category', models.ForeignKey(blank=True, help_text='Выберите категорию', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='titles', to='reviews.Category', verbose_name='Категория')),
                ('genre', models.ManyToManyField(help_text='Выберите жанр', related_name='titles', to='reviews.Genre', verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Произведение',
                'verbose_name_plural': 'Произведения',
            },
        ),
    ]
