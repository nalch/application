# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0029_auto_20160129_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('name_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='project',
            name='groups',
            field=models.ManyToManyField(to='nalch_application.Group'),
            preserve_default=True,
        ),
    ]
