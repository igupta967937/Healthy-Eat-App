# Generated by Django 2.0 on 2020-06-11 17:37

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('news', '0002_auto_20200611_1736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='article',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
