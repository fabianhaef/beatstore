# Generated by Django 3.2.5 on 2021-10-01 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='duki',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
