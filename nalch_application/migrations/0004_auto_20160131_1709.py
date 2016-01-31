# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0003_auto_20160131_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='technology',
            name='name_de',
            field=models.CharField(max_length=200, unique=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='technology',
            name='name_en',
            field=models.CharField(max_length=200, unique=True, null=True),
            preserve_default=True,
        ),
    ]
