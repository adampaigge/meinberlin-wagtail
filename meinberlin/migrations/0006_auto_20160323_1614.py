# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-23 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meinberlin', '0005_update_models_for_process_import'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adhocracyprocess',
            name='embed_url',
            field=models.URLField(unique=True),
        ),
        migrations.AlterField(
            model_name='adhocracyprocess',
            name='process_type',
            field=models.CharField(choices=[('adhocracy_meinberlin.resources.alexanderplatz.IProcess', 'Alexanderplatz'), ('adhocracy_meinberlin.resources.bplan.IProcess', 'Bebauungsplan'), ('adhocracy_meinberlin.resources.burgerhaushalt.IProcess', 'Bürgerhaushalt'), ('adhocracy_core.resources.proposal.IProposalVersion', 'Dialog'), ('adhocracy_meinberlin.resources.kiezkassen.IProcess', 'Kiezkasse'), ('adhocracy_meinberlin.resources.collaborative_text.IProcess', 'Kollaborative Textarbeit')], default='adhocracy_meinberlin.resources.kiezkassen.IProcess', max_length=255),
        ),
        migrations.AlterField(
            model_name='externalprocess',
            name='external_url',
            field=models.URLField(unique=True),
        ),
    ]