# Generated by Django 4.1.13 on 2024-05-23 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='billing_code',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='shipping_code',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='billing_code',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='shipping_code',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
