# Generated by Django 2.2 on 2020-06-25 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diets', '0002_auto_20200625_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weight',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]