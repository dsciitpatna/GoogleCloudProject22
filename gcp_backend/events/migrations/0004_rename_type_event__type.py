# Generated by Django 4.1.4 on 2022-12-21 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_subscription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='type',
            new_name='_type',
        ),
    ]
