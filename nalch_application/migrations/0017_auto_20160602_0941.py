# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0016_auto_20160209_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='template',
            field=models.TextField(default=b'photon', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tag',
            name='icon',
            field=models.CharField(default=b'', help_text=b'a bootstrap or font awesome icon, f.e. home, bullhorn, envelope, globe, etc.\nSee: http://getbootstrap.com/components/#glyphicons-glyphs', max_length=200, choices=[(b'home', 'home'), (b'bullhorn', 'bullhorn'), (b'envelope', 'envelope'), (b'globe', 'globe'), (b'gift', 'gift'), (b'phone-alt', 'phone-alt'), (b'earphone', 'earphone'), (b'thumbs-up', 'thumbs-up'), (b'check', 'check'), (b'wrench', 'wrench'), (b'phone', 'phone'), (b'mobile', 'mobile'), (b'map-marker', 'map-marker')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='technology',
            name='icon',
            field=models.CharField(default=b'', help_text=b'a bootstrap or font awesome icon, f.e. home, bullhorn, envelope, globe, etc.\nSee: http://getbootstrap.com/components/#glyphicons-glyphs', max_length=200, choices=[(b'home', 'home'), (b'bullhorn', 'bullhorn'), (b'envelope', 'envelope'), (b'globe', 'globe'), (b'gift', 'gift'), (b'phone-alt', 'phone-alt'), (b'earphone', 'earphone'), (b'thumbs-up', 'thumbs-up'), (b'check', 'check'), (b'wrench', 'wrench'), (b'phone', 'phone'), (b'mobile', 'mobile'), (b'map-marker', 'map-marker')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contactdetail',
            name='icon',
            field=models.CharField(default=b'', help_text=b'a bootstrap or font awesome icon, f.e. home, bullhorn, envelope, globe, etc.\nSee: http://getbootstrap.com/components/#glyphicons-glyphs', max_length=200, choices=[(b'home', 'home'), (b'bullhorn', 'bullhorn'), (b'envelope', 'envelope'), (b'globe', 'globe'), (b'gift', 'gift'), (b'phone-alt', 'phone-alt'), (b'earphone', 'earphone'), (b'thumbs-up', 'thumbs-up'), (b'check', 'check'), (b'wrench', 'wrench'), (b'phone', 'phone'), (b'mobile', 'mobile'), (b'map-marker', 'map-marker')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='knowledgelevel',
            name='icon',
            field=models.CharField(default=b'', help_text=b'a bootstrap or font awesome icon, f.e. home, bullhorn, envelope, globe, etc.\nSee: http://getbootstrap.com/components/#glyphicons-glyphs', max_length=200, choices=[(b'home', 'home'), (b'bullhorn', 'bullhorn'), (b'envelope', 'envelope'), (b'globe', 'globe'), (b'gift', 'gift'), (b'phone-alt', 'phone-alt'), (b'earphone', 'earphone'), (b'thumbs-up', 'thumbs-up'), (b'check', 'check'), (b'wrench', 'wrench'), (b'phone', 'phone'), (b'mobile', 'mobile'), (b'map-marker', 'map-marker')]),
            preserve_default=True,
        ),
    ]
