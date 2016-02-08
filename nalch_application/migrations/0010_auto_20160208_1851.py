# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0009_auto_20160208_1738'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkingArea',
            fields=[
                ('name_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('name_de', models.CharField(max_length=200, unique=True, null=True)),
                ('name_en', models.CharField(max_length=200, unique=True, null=True)),
                ('description', models.TextField()),
                ('description_de', models.TextField(null=True)),
                ('description_en', models.TextField(null=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('tags', models.ManyToManyField(to='nalch_application.Tag', null=True, blank=True)),
                ('technologies', models.ManyToManyField(to='nalch_application.Technology', null=True, blank=True)),
                ('user', models.ForeignKey(to='nalch_application.Applicant')),
            ],
            options={
                'ordering': ('order',),
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='areaofinterest',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='areaofinterest',
            name='technologies',
        ),
        migrations.RemoveField(
            model_name='areaofinterest',
            name='user',
        ),
        migrations.DeleteModel(
            name='AreaOfInterest',
        ),
    ]
