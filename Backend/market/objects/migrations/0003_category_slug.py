# Generated by Django 4.1.5 on 2023-02-28 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0002_item_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
