# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0034_group_short_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='short_name_de',
            field=models.CharField(max_length=25, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='short_name_en',
            field=models.CharField(max_length=25, null=True),
            preserve_default=True,
        ),
    ]
