# Generated by Django 4.2 on 2023-04-24 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Нименование товара')),
                ('description', models.CharField(max_length=1000, verbose_name='Описание товара')),
                ('type', models.CharField(max_length=50, verbose_name='Тип устройства')),
                ('аggregation', models.CharField(max_length=50, verbose_name='Агрегатирование')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название компании-поставщика')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_date', models.DateField(default='2023-01-01', verbose_name='Дата поставки')),
                ('delivery_price', models.IntegerField(max_length=20, verbose_name='Цена ед. товара, руб.')),
                ('quantity_product', models.IntegerField(verbose_name='Количество товара, шт.')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='example_app.product', verbose_name='Товар')),
                ('supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='example_app.supplier', verbose_name='Поставщик')),
            ],
        ),
    ]
