# Generated by Django 4.1.3 on 2024-01-16 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_page', '0003_myfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Опубликовано'),
        ),
        migrations.AddField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации'),
        ),
    ]
