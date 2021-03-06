# Generated by Django 3.2.4 on 2021-06-19 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_planning', '0007_alter_brazilbill_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrazilShopping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=50, verbose_name='item')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price')),
            ],
            options={
                'verbose_name': "Brazil's Shopping",
                'verbose_name_plural': "Brazil's Shoppings",
            },
        ),
    ]
