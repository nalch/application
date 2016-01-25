# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0013_auto_20160125_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='short_name',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='short_name_de',
            field=models.CharField(max_length=25, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='short_name_en',
            field=models.CharField(max_length=25, null=True),
            preserve_default=True,
        ),
    ]
