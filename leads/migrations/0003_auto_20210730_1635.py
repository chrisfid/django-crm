# Generated by Django 3.1.4 on 2021-07-30 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_auto_20210730_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_agent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_organizer',
            field=models.BooleanField(default=True),
        ),
    ]
