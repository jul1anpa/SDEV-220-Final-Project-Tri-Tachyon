# Generated by Django 4.2.6 on 2023-10-13 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holder', '0003_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cart_id',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
    ]
