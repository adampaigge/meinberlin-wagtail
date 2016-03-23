# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-22 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meinberlin', '0004_adhocracypage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adhocracyprocess',
            name='embed_code',
        ),
        migrations.AddField(
            model_name='adhocracyprocess',
            name='embed_url',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='adhocracyprocess',
            name='process_type',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='process',
            name='image_copyright',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]