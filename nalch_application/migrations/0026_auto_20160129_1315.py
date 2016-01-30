# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0025_weightedtag_weight'),
    ]

    operations = [
        migrations.CreateModel(
            name='KnowlegdeLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weight', models.CharField(default=b'', max_length=200, choices=[(b'basic', 'basic knowledge'), (b'working', 'working knowledge'), (b'advanced', 'advanced knowledge')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='weightedtag',
            name='weight',
            field=models.ForeignKey(to='nalch_application.KnowlegdeLevel'),
            preserve_default=True,
        ),
    ]
