# Generated by Django 4.2.3 on 2023-08-06 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0012_remove_productseries_subcategory_delete_products_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSeries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='Productseries_img')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='Productseries_img')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='Productseries_img')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='Productseries_img')),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('slug', models.SlugField()),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomapp.subcategory')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSegment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=200)),
                ('name2', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomapp.category')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomapp.subcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_img')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='product_img2')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='product_img3')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='product_img4')),
                ('description', models.CharField(max_length=500)),
                ('disc_price', models.IntegerField()),
                ('org_price', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('slug', models.SlugField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomapp.category')),
                ('productsegment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomapp.productsegment')),
                ('productseries', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomapp.productseries')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomapp.subcategory')),
            ],
        ),
    ]
