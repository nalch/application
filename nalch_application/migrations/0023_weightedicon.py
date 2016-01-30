# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0022_auto_20160129_1300'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeightedIcon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('icon', models.ForeignKey(to='nalch_application.Icon')),
                ('tag', models.ForeignKey(to='nalch_application.Tag')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
