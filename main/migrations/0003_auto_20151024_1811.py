# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20151023_1738'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Place',
        ),
        migrations.RemoveField(
            model_name='tweet',
            name='favorites',
        ),
        migrations.RemoveField(
            model_name='tweet',
            name='lang',
        ),
        migrations.AddField(
            model_name='tweet',
            name='created_at',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tweet',
            name='location',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tweet',
            name='profile_image_url',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tweet',
            name='screen_name',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tweet',
            name='source',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tweet',
            name='time_zone',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
