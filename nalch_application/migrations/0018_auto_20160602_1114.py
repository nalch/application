# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0017_auto_20160602_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='template',
            field=models.CharField(default=b'photon', max_length=250, null=True, blank=True, choices=[(b'photon', 'photon')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contactdetail',
            name='icon',
            field=models.CharField(default=b'', help_text=b'a bootstrap or font awesome icon, f.e. home, bullhorn, envelope, globe, etc.\nSee: http://getbootstrap.com/components/#glyphicons-glyphs', max_length=200, choices=[(b'configurationmanagement', 'configurationmanagement'), (b'thumbs-up', 'thumbs-up'), (b'earphone', 'earphone'), (b'gift', 'gift'), (b'nginx', 'nginx'), (b'mobile', 'mobile'), (b'globe', 'globe'), (b'map-marker', 'map-marker'), (b'envelope', 'envelope'), (b'nodejs', 'nodejs'), (b'phone', 'phone'), (b'kibana', 'kibana'), (b'phone-alt', 'phone-alt'), (b'bullhorn', 'bullhorn'), (b'wrench', 'wrench'), (b'home', 'home'), (b'check', 'check')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='knowledgelevel',
            name='icon',
            field=models.CharField(default=b'', help_text=b'a bootstrap or font awesome icon, f.e. home, bullhorn, envelope, globe, etc.\nSee: http://getbootstrap.com/components/#glyphicons-glyphs', max_length=200, choices=[(b'configurationmanagement', 'configurationmanagement'), (b'thumbs-up', 'thumbs-up'), (b'earphone', 'earphone'), (b'gift', 'gift'), (b'nginx', 'nginx'), (b'mobile', 'mobile'), (b'globe', 'globe'), (b'map-marker', 'map-marker'), (b'envelope', 'envelope'), (b'nodejs', 'nodejs'), (b'phone', 'phone'), (b'kibana', 'kibana'), (b'phone-alt', 'phone-alt'), (b'bullhorn', 'bullhorn'), (b'wrench', 'wrench'), (b'home', 'home'), (b'check', 'check')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tag',
            name='icon',
            field=models.CharField(default=b'', help_text=b'a bootstrap or font awesome icon, f.e. home, bullhorn, envelope, globe, etc.\nSee: http://getbootstrap.com/components/#glyphicons-glyphs', max_length=200, choices=[(b'configurationmanagement', 'configurationmanagement'), (b'thumbs-up', 'thumbs-up'), (b'earphone', 'earphone'), (b'gift', 'gift'), (b'nginx', 'nginx'), (b'mobile', 'mobile'), (b'globe', 'globe'), (b'map-marker', 'map-marker'), (b'envelope', 'envelope'), (b'nodejs', 'nodejs'), (b'phone', 'phone'), (b'kibana', 'kibana'), (b'phone-alt', 'phone-alt'), (b'bullhorn', 'bullhorn'), (b'wrench', 'wrench'), (b'home', 'home'), (b'check', 'check')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='technology',
            name='icon',
            field=models.CharField(default=b'', help_text=b'a bootstrap or font awesome icon, f.e. home, bullhorn, envelope, globe, etc.\nSee: http://getbootstrap.com/components/#glyphicons-glyphs', max_length=200, choices=[(b'configurationmanagement', 'configurationmanagement'), (b'thumbs-up', 'thumbs-up'), (b'earphone', 'earphone'), (b'gift', 'gift'), (b'nginx', 'nginx'), (b'mobile', 'mobile'), (b'globe', 'globe'), (b'map-marker', 'map-marker'), (b'envelope', 'envelope'), (b'nodejs', 'nodejs'), (b'phone', 'phone'), (b'kibana', 'kibana'), (b'phone-alt', 'phone-alt'), (b'bullhorn', 'bullhorn'), (b'wrench', 'wrench'), (b'home', 'home'), (b'check', 'check')]),
            preserve_default=True,
        ),
    ]
