# Generated by Django 4.1.13 on 2024-05-23 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_profile_billing_code_profile_shipping_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='stripe_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
