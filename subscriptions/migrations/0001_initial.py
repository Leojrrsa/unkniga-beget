# Generated by Django 4.2.7 on 2024-02-28 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(choices=[('01/02', 'Январь-Февраль'), ('03', 'Март'), ('04', 'Апрель'), ('05', 'Май'), ('06', 'Июнь'), ('07/08', 'Июль-Август'), ('09', 'Сентябрь'), ('10', 'Октябрь'), ('11', 'Ноябрь'), ('12', 'Декабрь')], max_length=5, unique=True, verbose_name='Код месяца')),
                ('name', models.CharField(max_length=20, verbose_name='Название месяца')),
            ],
        ),
        migrations.CreateModel(
            name='CorporateSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('paper', 'Бумажный вариант'), ('electronic', 'Электронный вариант')], max_length=10, verbose_name='Варианты получения журнала')),
                ('year', models.CharField(default='2024', max_length=4, verbose_name='Год')),
                ('amount', models.IntegerField(default=1, verbose_name='Количество экземпляров')),
                ('org_name', models.TextField(verbose_name='Наименование организации')),
                ('phone', models.CharField(max_length=12, verbose_name='Телефон')),
                ('inn', models.CharField(max_length=12, verbose_name='ИНН')),
                ('kpp', models.CharField(max_length=9, verbose_name='КПП')),
                ('real_address', models.TextField(verbose_name='Адрес фактический')),
                ('corporate_address', models.TextField(verbose_name='Адрес Юридический')),
                ('email', models.EmailField(max_length=100, verbose_name='Электронный почтовый адрес e-mail')),
                ('contact', models.CharField(max_length=50, verbose_name='Контактное лицо')),
                ('issues', models.ManyToManyField(to='subscriptions.month', verbose_name='Выберите нужные номера')),
            ],
        ),
    ]
