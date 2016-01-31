# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0037_auto_20160131_1303'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='tags',
            new_name='tags_middle',
        ),
    ]
