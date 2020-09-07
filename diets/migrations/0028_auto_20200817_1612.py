# Generated by Django 2.2 on 2020-08-17 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hairstyle', '0010_auto_20200810_1008'),
        ('diets', '0027_auto_20200814_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diet',
            name='breakfast',
        ),
        migrations.AddField(
            model_name='diet',
            name='breakfast',
            field=models.ManyToManyField(blank=True, related_name='breakfast', to='hairstyle.Recipe'),
        ),
        migrations.AlterField(
            model_name='diet',
            name='dinner',
            field=models.ManyToManyField(blank=True, related_name='dinner', to='hairstyle.Recipe'),
        ),
        migrations.RemoveField(
            model_name='diet',
            name='lunch',
        ),
        migrations.AddField(
            model_name='diet',
            name='lunch',
            field=models.ManyToManyField(blank=True, related_name='lunch', to='hairstyle.Recipe'),
        ),
    ]