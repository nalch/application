# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0009_auto_20160122_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='address_de',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='applicant',
            name='address_en',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contactdetail',
            name='text_de',
            field=models.TextField(default=b'', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contactdetail',
            name='text_en',
            field=models.TextField(default=b'', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='description_de',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='description_en',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='name_de',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='name_en',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]
