# Generated by Django 4.1.7 on 2023-05-27 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0005_rename_order_id_orderitem_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='data',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
