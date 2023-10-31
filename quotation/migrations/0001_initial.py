# Generated by Django 4.1.9 on 2023-10-31 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('message', models.TextField()),
                ('status', models.CharField(choices=[('pending', 'Pending Payment'), ('paid', 'Paid'), ('confirmed', 'Confirmed')], default='pending', max_length=10)),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
