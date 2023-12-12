# Generated by Django 4.1.9 on 2023-12-10 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_subcategory_alter_productcategory_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcoupon',
            options={'verbose_name_plural': 'Product Coupon'},
        ),
        migrations.AlterField(
            model_name='productbrand',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='productbrand',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='productcoupon',
            name='code',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]