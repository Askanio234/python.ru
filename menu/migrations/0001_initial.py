# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 22:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cards_api', '0002_auto_20170726_1045'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('url', models.URLField(blank=True, null=True)),
                ('card_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cards_api.CardCategory')),
            ],
        ),
    ]
