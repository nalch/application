# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0032_auto_20160131_1021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='short_name_de',
        ),
        migrations.RemoveField(
            model_name='project',
            name='short_name_en',
        ),
    ]
