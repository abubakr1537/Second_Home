# Generated by Django 2.1.5 on 2020-01-10 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='address',
            field=models.CharField(default='Jurye', max_length=225),
            preserve_default=False,
        ),
    ]
