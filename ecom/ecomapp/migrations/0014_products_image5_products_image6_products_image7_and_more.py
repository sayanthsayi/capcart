# Generated by Django 4.2.3 on 2023-08-16 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0013_productseries_productsegment_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='product_img5'),
        ),
        migrations.AddField(
            model_name='products',
            name='image6',
            field=models.ImageField(blank=True, null=True, upload_to='product_img6'),
        ),
        migrations.AddField(
            model_name='products',
            name='image7',
            field=models.ImageField(blank=True, null=True, upload_to='product_img7'),
        ),
        migrations.AddField(
            model_name='products',
            name='image8',
            field=models.ImageField(blank=True, null=True, upload_to='product_img8'),
        ),
    ]