# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0014_auto_20160125_2130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('name_de', models.CharField(max_length=200, null=True)),
                ('name_en', models.CharField(max_length=200, null=True)),
                ('file', models.FileField(upload_to=b'')),
                ('project', models.ForeignKey(blank=True, to='nalch_application.Project', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
