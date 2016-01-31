# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0002_auto_20160131_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('name_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='project',
            name='technologies',
            field=models.ManyToManyField(to='nalch_application.Technology'),
            preserve_default=True,
        ),
    ]
