# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0006_auto_20160202_2237'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaOfInterest',
            fields=[
                ('name_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
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
    ]