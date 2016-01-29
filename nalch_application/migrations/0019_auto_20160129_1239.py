# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0018_auto_20160129_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='translatablenamemixin_ptr',
        ),
        migrations.DeleteModel(
            name='TranslatableNameMixin',
        ),
        migrations.AddField(
            model_name='tag',
            name='name',
            field=models.CharField(default='noname', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='name_de',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tag',
            name='name_en',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tag',
            name='name_id',
            field=models.AutoField(default=1, serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]
