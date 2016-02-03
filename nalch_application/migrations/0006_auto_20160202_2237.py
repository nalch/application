# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0005_auto_20160131_1825'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ('order',)},
        ),
        migrations.AddField(
            model_name='project',
            name='order',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contactdetail',
            name='icon',
            field=models.CharField(default=b'', help_text=b'a bootstrap icon, f.e. home, bullhorn, envelope, globe, etc.\nSee: http://getbootstrap.com/components/#glyphicons-glyphs', max_length=200, choices=[(b'home', 'home'), (b'bullhorn', 'bullhorn'), (b'envelope', 'envelope'), (b'globe', 'globe'), (b'gift', 'gift'), (b'phone-alt', 'phone-alt'), (b'earphone', 'earphone'), (b'thumbs-up', 'thumbs-up'), (b'check', 'check'), (b'wrench', 'wrench')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='knowledgelevel',
            name='icon',
            field=models.CharField(default=b'', help_text=b'a bootstrap icon, f.e. home, bullhorn, envelope, globe, etc.\nSee: http://getbootstrap.com/components/#glyphicons-glyphs', max_length=200, choices=[(b'home', 'home'), (b'bullhorn', 'bullhorn'), (b'envelope', 'envelope'), (b'globe', 'globe'), (b'gift', 'gift'), (b'phone-alt', 'phone-alt'), (b'earphone', 'earphone'), (b'thumbs-up', 'thumbs-up'), (b'check', 'check'), (b'wrench', 'wrench')]),
            preserve_default=True,
        ),
    ]
