# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0008_auto_20160122_1210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicant',
            name='details',
        ),
        migrations.AddField(
            model_name='contactdetail',
            name='applicant',
            field=models.ForeignKey(blank=True, to='nalch_application.Applicant', null=True),
            preserve_default=True,
        ),
    ]
