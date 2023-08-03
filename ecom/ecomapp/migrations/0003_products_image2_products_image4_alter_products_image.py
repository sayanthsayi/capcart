# Generated by Django 4.2.3 on 2023-08-02 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0002_category_series'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='product_img2'),
        ),
        migrations.AddField(
            model_name='products',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='product_img4'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_img'),
        ),
    ]
