# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0014_auto_20160209_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='areas_of_expertise',
            field=models.ManyToManyField(related_name='expertises', null=True, to='nalch_application.AreaOfKnowledge', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='applicant',
            name='areas_of_interest',
            field=models.ManyToManyField(related_name='interests', null=True, to='nalch_application.AreaOfInterest', blank=True),
            preserve_default=True,
        ),
    ]
