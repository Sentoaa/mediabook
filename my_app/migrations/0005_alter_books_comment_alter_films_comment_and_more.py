# Generated by Django 4.2.3 on 2023-07-15 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_alter_books_img_url_alter_films_img_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='comment',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='films',
            name='comment',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='readedbooks',
            name='comment',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='series',
            name='comment',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='watchedfilms',
            name='comment',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='watchedseries',
            name='comment',
            field=models.TextField(blank=True, default=''),
        ),
    ]