# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0022_auto_20160610_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='user',
            field=models.OneToOneField(to='nalch_application.Applicant'),
            preserve_default=True,
        ),
    ]
