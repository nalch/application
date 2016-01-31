# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0033_auto_20160131_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='short_name',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
    ]
