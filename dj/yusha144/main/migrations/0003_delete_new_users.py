# Generated by Django 5.0.4 on 2024-05-19 04:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0002_alter_new_users_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='new_users',
        ),
    ]
