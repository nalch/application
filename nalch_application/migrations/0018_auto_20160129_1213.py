# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0017_tag_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='TranslatableNameMixin',
            fields=[
                ('name_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('name_de', models.CharField(max_length=200, null=True)),
                ('name_en', models.CharField(max_length=200, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='tag',
            name='id',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='name',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='name_de',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='name_en',
        ),
        migrations.AddField(
            model_name='tag',
            name='translatablenamemixin_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=1, serialize=False, to='nalch_application.TranslatableNameMixin'),
            preserve_default=False,
        ),
    ]
