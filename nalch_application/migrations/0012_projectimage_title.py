# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0011_auto_20160125_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectimage',
            name='title',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
