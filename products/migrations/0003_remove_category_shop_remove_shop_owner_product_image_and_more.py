# Generated by Django 5.1.4 on 2024-12-10 10:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_product_stock_product_shop_and_more'),
        ('users', '0002_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='shop',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='owner',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='shop',
            name='seller',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='users.seller'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.shop'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='description',
            field=models.TextField(),
        ),
    ]
