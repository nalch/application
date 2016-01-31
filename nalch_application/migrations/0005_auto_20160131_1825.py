# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0004_auto_20160131_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='technologies',
            field=models.ManyToManyField(to='nalch_application.Technology', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='weightedtag',
            name='project',
            field=models.ForeignKey(blank=True, to='nalch_application.Project', null=True),
            preserve_default=True,
        ),
    ]
