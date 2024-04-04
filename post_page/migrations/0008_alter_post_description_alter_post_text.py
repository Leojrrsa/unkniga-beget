# Generated by Django 4.1.3 on 2024-02-21 11:31

from django.db import migrations
import django_summernote.fields


class Migration(migrations.Migration):

    dependencies = [
        ('post_page', '0007_alter_post_card_display'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=django_summernote.fields.SummernoteTextField(max_length=200, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=django_summernote.fields.SummernoteTextField(),
        ),
    ]