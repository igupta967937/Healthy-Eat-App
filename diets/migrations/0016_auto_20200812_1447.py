# Generated by Django 2.2 on 2020-08-12 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diets', '0015_auto_20200810_1137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diet',
            name='subscriber',
        ),
        migrations.AddField(
            model_name='diet',
            name='subscriber',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='subscriber', to=settings.AUTH_USER_MODEL),
        ),
    ]
