# Generated by Django 4.1.7 on 2023-04-17 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0002_shop_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]