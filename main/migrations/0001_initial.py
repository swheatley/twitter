# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('favourites_count', models.IntegerField(null=True, blank=True)),
                ('friends_count', models.IntegerField(null=True, blank=True)),
                ('listed_count', models.IntegerField(null=True, blank=True)),
                ('statuses_count', models.IntegerField(null=True, blank=True)),
                ('favorite_count', models.IntegerField(null=True, blank=True)),
                ('retweet_count', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profile_background_color', models.CharField(max_length=50, null=True, blank=True)),
                ('profile_banner_url', models.CharField(max_length=50, null=True, blank=True)),
            ],
        ),
    ]
