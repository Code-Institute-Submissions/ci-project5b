# Generated by Django 4.1.13 on 2024-05-22 15:27

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0008_support'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('number', models.CharField(max_length=50, unique=True)),
                ('billing_name', models.CharField(max_length=255)),
                ('billing_address', models.TextField()),
                ('billing_phone', models.CharField(blank=True, max_length=20)),
                ('shipping_name', models.CharField(blank=True, max_length=255)),
                ('shipping_address', models.TextField(blank=True)),
                ('shipping_phone', models.CharField(blank=True, max_length=20)),
                ('items_total', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('delivery_amount', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('vat_amount', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('order_total', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SalesOrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
                ('sales_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='shop.salesorder')),
            ],
            options={
                'unique_together': {('sales_order', 'product')},
            },
        ),
    ]
