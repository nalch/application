# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0015_attachment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('name_de', models.CharField(max_length=200, null=True)),
                ('name_en', models.CharField(max_length=200, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='project',
            name='ended',
        ),
        migrations.RemoveField(
            model_name='project',
            name='started',
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(to='nalch_application.Tag'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='attachment',
            name='project',
            field=models.ForeignKey(default=1, to='nalch_application.Project'),
            preserve_default=False,
        ),
    ]
