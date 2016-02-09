# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0013_auto_20160209_1837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workingarea',
            name='description_de',
        ),
        migrations.RemoveField(
            model_name='workingarea',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='workingarea',
            name='name_de',
        ),
        migrations.RemoveField(
            model_name='workingarea',
            name='name_en',
        ),
        migrations.AddField(
            model_name='areaofinterest',
            name='description_de',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='areaofinterest',
            name='description_en',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='areaofinterest',
            name='name_de',
            field=models.CharField(max_length=200, unique=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='areaofinterest',
            name='name_en',
            field=models.CharField(max_length=200, unique=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='areaofknowledge',
            name='description_de',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='areaofknowledge',
            name='description_en',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='areaofknowledge',
            name='name_de',
            field=models.CharField(max_length=200, unique=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='areaofknowledge',
            name='name_en',
            field=models.CharField(max_length=200, unique=True, null=True),
            preserve_default=True,
        ),
    ]
