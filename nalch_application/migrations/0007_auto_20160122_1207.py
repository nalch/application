# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0006_contactdetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicant',
            name='phonenumber',
        ),
        migrations.RemoveField(
            model_name='applicant',
            name='url',
        ),
    ]
