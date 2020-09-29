# Generated by Django 2.2.15 on 2020-09-25 00:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hairstyle', '0014_auto_20200925_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format '+123456789'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
