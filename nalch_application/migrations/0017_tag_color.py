# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorful.fields


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0016_auto_20160127_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='color',
            field=colorful.fields.RGBColorField(default='#337ab7'),
            preserve_default=False,
        ),
    ]
