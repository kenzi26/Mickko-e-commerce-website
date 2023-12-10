# Generated by Django 4.1.9 on 2023-12-10 14:15

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biodata', '0002_rename_emails_biodata_work_emails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biodata',
            name='work_emails',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(max_length=254), help_text='Enter email addresses separated by commas.', size=None),
        ),
    ]
