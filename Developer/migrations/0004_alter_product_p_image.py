# Generated by Django 4.2.1 on 2023-11-03 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Developer', '0003_brands_product_p_image_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='p_image',
            field=models.ImageField(null=True, upload_to='ProductImages/'),
        ),
    ]
