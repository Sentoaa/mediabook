# Generated by Django 4.2.3 on 2023-07-10 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='title',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='films',
            name='title',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='readedbooks',
            name='title',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='series',
            name='title',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='watchedfilms',
            name='title',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='watchedseries',
            name='title',
            field=models.TextField(),
        ),
    ]
