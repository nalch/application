# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0020_auto_20160129_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attachment',
            name='id',
        ),
        migrations.RemoveField(
            model_name='contactdetail',
            name='id',
        ),
        migrations.RemoveField(
            model_name='contactdetail',
            name='text',
        ),
        migrations.RemoveField(
            model_name='contactdetail',
            name='text_de',
        ),
        migrations.RemoveField(
            model_name='contactdetail',
            name='text_en',
        ),
        migrations.RemoveField(
            model_name='project',
            name='id',
        ),
        migrations.RemoveField(
            model_name='projectimage',
            name='id',
        ),
        migrations.RemoveField(
            model_name='projectimage',
            name='title',
        ),
        migrations.RemoveField(
            model_name='projectimage',
            name='title_de',
        ),
        migrations.RemoveField(
            model_name='projectimage',
            name='title_en',
        ),
        migrations.AddField(
            model_name='attachment',
            name='name_id',
            field=models.AutoField(default=1, serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactdetail',
            name='name',
            field=models.CharField(default='name', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactdetail',
            name='name_de',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contactdetail',
            name='name_en',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contactdetail',
            name='name_id',
            field=models.AutoField(default=1, serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='name_id',
            field=models.AutoField(default=1, serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectimage',
            name='name',
            field=models.CharField(default='name', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectimage',
            name='name_de',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='projectimage',
            name='name_en',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='projectimage',
            name='name_id',
            field=models.AutoField(default=1, serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]
