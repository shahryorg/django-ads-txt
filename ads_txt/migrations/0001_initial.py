# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-03 09:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=100, verbose_name='Domain')),
                ('account_id', models.CharField(max_length=255, verbose_name='account ID')),
                ('account_type', models.CharField(choices=[('DIRECT', 'DIRECT'), ('RESELLER', 'RESELLER')], max_length=100, verbose_name='Account Type')),
                ('authority_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='Authority ID')),
                ('sites', models.ManyToManyField(related_name='adstxt', to='sites.Site', verbose_name='sites')),
            ],
            options={
                'verbose_name_plural': 'rules',
                'verbose_name': 'rule',
            },
        ),
    ]