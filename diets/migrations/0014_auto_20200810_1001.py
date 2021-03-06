# Generated by Django 2.2 on 2020-08-10 10:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diets', '0013_diet_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diet',
            name='subscriber',
        ),
        migrations.AddField(
            model_name='diet',
            name='subscriber',
            field=models.ManyToManyField(blank=True, related_name='subscriber', to=settings.AUTH_USER_MODEL),
        ),
    ]
