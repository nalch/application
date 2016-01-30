# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0027_auto_20160129_1316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactdetail',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='knowledgelevel',
            name='icon',
        ),
        migrations.AddField(
            model_name='icon',
            name='contact_detail',
            field=models.ForeignKey(default=1, to='nalch_application.ContactDetail'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='icon',
            name='knowledge_level',
            field=models.ForeignKey(default=1, to='nalch_application.KnowledgeLevel'),
            preserve_default=False,
        ),
    ]
