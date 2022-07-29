# Generated by Django 2.2.16 on 2022-07-29 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='category',
            constraint=models.UniqueConstraint(fields=('name', 'slug'), name='exclude the re-creation of the сategory'),
        ),
        migrations.AddConstraint(
            model_name='genre',
            constraint=models.UniqueConstraint(fields=('name', 'slug'), name='exclude the re-creation of the genre'),
        ),
        migrations.AddConstraint(
            model_name='title',
            constraint=models.UniqueConstraint(fields=('name', 'year'), name='exclude the re-creation of the titles'),
        ),
    ]
