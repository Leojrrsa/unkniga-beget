# Generated by Django 4.1.3 on 2024-02-28 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_page', '0010_alter_post_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='page_journal',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Номер страницы в журнале'),
        ),
    ]
