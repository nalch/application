# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0007_auto_20160122_1207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactdetail',
            name='applicant',
        ),
        migrations.AddField(
            model_name='applicant',
            name='details',
            field=models.ForeignKey(blank=True, to='nalch_application.ContactDetail', null=True),
            preserve_default=True,
        ),
    ]
