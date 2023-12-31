# Generated by Django 4.2.3 on 2023-08-21 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_checkout_address_district_checkout_address_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='district',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
