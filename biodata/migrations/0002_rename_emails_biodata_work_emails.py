# Generated by Django 4.1.9 on 2023-11-05 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biodata', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='biodata',
            old_name='emails',
            new_name='work_emails',
        ),
    ]
