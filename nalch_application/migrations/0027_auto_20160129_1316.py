# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0026_auto_20160129_1315'),
    ]

    operations = [
        migrations.CreateModel(
            name='KnowledgeLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weight', models.CharField(default=b'', max_length=200, choices=[(b'basic', 'basic knowledge'), (b'working', 'working knowledge'), (b'advanced', 'advanced knowledge')])),
                ('icon', models.ForeignKey(to='nalch_application.Icon')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='weightedtag',
            name='icon',
        ),
        migrations.AlterField(
            model_name='weightedtag',
            name='weight',
            field=models.ForeignKey(to='nalch_application.KnowledgeLevel'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='KnowlegdeLevel',
        ),
    ]
