# Generated by Django 4.2.1 on 2023-11-05 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Developer', '0008_purchase_bill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='bill',
            field=models.FileField(blank=True, null=True, upload_to='Purchase Bills'),
        ),
    ]
