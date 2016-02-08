# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0010_auto_20160208_1851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workingarea',
            name='user',
        ),
        migrations.AddField(
            model_name='applicant',
            name='areas_of_expertise',
            field=models.ManyToManyField(related_name='expertises', null=True, to='nalch_application.WorkingArea', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='applicant',
            name='areas_of_interest',
            field=models.ManyToManyField(related_name='interests', null=True, to='nalch_application.WorkingArea', blank=True),
            preserve_default=True,
        ),
    ]
