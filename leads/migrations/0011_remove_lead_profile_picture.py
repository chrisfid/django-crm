# Generated by Django 3.1.4 on 2021-08-12 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0010_remove_lead_converted_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='profile_picture',
        ),
    ]
