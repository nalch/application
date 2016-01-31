# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0031_auto_20160130_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='description_de',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='description_en',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contactdetail',
            name='icon',
            field=models.CharField(default=b'', help_text=b'a bootstrap icon, f.e. home, bullhorn, envelope, globe, etc.\nSee: http://getbootstrap.com/components/#glyphicons-glyphs', max_length=200, choices=[(b'home', 'home'), (b'bullhorn', 'bullhorn'), (b'envelope', 'envelope'), (b'globe', 'globe'), (b'gift', 'gift'), (b'earphone', 'earphone'), (b'thumbs-up', 'thumbs-up'), (b'check', 'check'), (b'wrench', 'wrench')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='knowledgelevel',
            name='icon',
            field=models.CharField(default=b'', help_text=b'a bootstrap icon, f.e. home, bullhorn, envelope, globe, etc.\nSee: http://getbootstrap.com/components/#glyphicons-glyphs', max_length=200, choices=[(b'home', 'home'), (b'bullhorn', 'bullhorn'), (b'envelope', 'envelope'), (b'globe', 'globe'), (b'gift', 'gift'), (b'earphone', 'earphone'), (b'thumbs-up', 'thumbs-up'), (b'check', 'check'), (b'wrench', 'wrench')]),
            preserve_default=True,
        ),
    ]
