# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0002_auto_20161107_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='short_description',
            field=models.TextField(default=b'', max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='short_description_de',
            field=models.TextField(default=b'', max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='short_description_en',
            field=models.TextField(default=b'', max_length=255, null=True),
            preserve_default=True,
        ),
    ]
