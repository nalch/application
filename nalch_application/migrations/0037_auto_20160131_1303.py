# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0036_auto_20160131_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='name',
            field=models.CharField(unique=True, max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='attachment',
            name='name_de',
            field=models.CharField(max_length=200, unique=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='attachment',
            name='name_en',
            field=models.CharField(max_length=200, unique=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contactdetail',
            name='name',
            field=models.CharField(unique=True, max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contactdetail',
            name='name_de',
            field=models.CharField(max_length=200, unique=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contactdetail',
            name='name_en',
            field=models.CharField(max_length=200, unique=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(unique=True, max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='name_de',
            field=models.CharField(max_length=200, unique=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='name_en',
            field=models.CharField(max_length=200, unique=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='short_name',
            field=models.CharField(unique=True, max_length=25),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='short_name_de',
            field=models.CharField(max_length=25, unique=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='short_name_en',
            field=models.CharField(max_length=25, unique=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(unique=True, max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='name_de',
            field=models.CharField(max_length=200, unique=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='name_en',
            field=models.CharField(max_length=200, unique=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='short_name',
            field=models.CharField(unique=True, max_length=25),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='short_name_de',
            field=models.CharField(max_length=25, unique=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='short_name_en',
            field=models.CharField(max_length=25, unique=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='name',
            field=models.CharField(unique=True, max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='name_de',
            field=models.CharField(max_length=200, unique=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='name_en',
            field=models.CharField(max_length=200, unique=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(unique=True, max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tag',
            name='name_de',
            field=models.CharField(max_length=200, unique=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tag',
            name='name_en',
            field=models.CharField(max_length=200, unique=True, null=True),
            preserve_default=True,
        ),
    ]
