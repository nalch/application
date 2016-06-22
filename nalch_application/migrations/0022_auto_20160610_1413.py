# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0021_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='description',
            name='description_de',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='description',
            name='description_en',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
