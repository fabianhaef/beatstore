# Generated by Django 3.2.5 on 2021-10-04 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_product_duki'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='duki',
        ),
    ]
