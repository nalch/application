# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0015_auto_20160209_1842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workingarea',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='workingarea',
            name='technologies',
        ),
        migrations.DeleteModel(
            name='WorkingArea',
        ),
    ]
