# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0030_auto_20160130_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='name_de',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='name_en',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]
