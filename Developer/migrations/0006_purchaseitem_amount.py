# Generated by Django 4.2.1 on 2023-11-04 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Developer', '0005_rename_purchase_id_purchase_purchase_invoice_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseitem',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
