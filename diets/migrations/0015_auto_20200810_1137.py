# Generated by Django 2.2 on 2020-08-10 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hairstyle', '0010_auto_20200810_1008'),
        ('diets', '0014_auto_20200810_1001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diet',
            name='breakfast',
        ),
        migrations.AddField(
            model_name='diet',
            name='breakfast',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='breakfast', to='hairstyle.Recipe'),
        ),
    ]