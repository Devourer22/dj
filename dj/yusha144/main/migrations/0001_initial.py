# Generated by Django 5.0.4 on 2024-05-17 13:47

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='new_users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=20, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, verbose_name='Имя')),
                ('second_name', models.CharField(max_length=25, verbose_name='Фамилия')),
                ('group', models.CharField(max_length=10, verbose_name='Группа')),
            ],
        ),
    ]