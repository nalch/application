# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0023_weightedicon'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeightedTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('icon', models.ForeignKey(to='nalch_application.Icon')),
                ('project', models.ForeignKey(to='nalch_application.Project')),
                ('tag', models.ForeignKey(to='nalch_application.Tag')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='weightedicon',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='weightedicon',
            name='tag',
        ),
        migrations.DeleteModel(
            name='WeightedIcon',
        ),
    ]
