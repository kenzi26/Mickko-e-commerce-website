# Generated by Django 4.1.5 on 2023-10-31 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, to='product.producttag'),
        ),
    ]
