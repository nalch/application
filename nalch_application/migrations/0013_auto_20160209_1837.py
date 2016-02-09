# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0012_areaofinterest_areaofknowledge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicant',
            name='areas_of_expertise',
        ),
        migrations.RemoveField(
            model_name='applicant',
            name='areas_of_interest',
        ),
    ]
