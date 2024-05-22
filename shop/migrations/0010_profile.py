# Generated by Django 4.1.13 on 2024-05-22 19:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0009_salesorder_salesorderitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billing_name', models.CharField(max_length=255)),
                ('billing_address', models.TextField()),
                ('billing_phone', models.CharField(blank=True, max_length=20)),
                ('shipping_name', models.CharField(blank=True, max_length=255)),
                ('shipping_address', models.TextField(blank=True)),
                ('shipping_phone', models.CharField(blank=True, max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
