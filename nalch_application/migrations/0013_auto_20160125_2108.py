# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0012_projectimage_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectimage',
            name='title_de',
            field=models.CharField(max_length=500, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='projectimage',
            name='title_en',
            field=models.CharField(max_length=500, null=True),
            preserve_default=True,
        ),
    ]
