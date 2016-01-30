# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0028_auto_20160129_1348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='icon',
            name='contact_detail',
        ),
        migrations.RemoveField(
            model_name='icon',
            name='knowledge_level',
        ),
        migrations.DeleteModel(
            name='Icon',
        ),
        migrations.AddField(
            model_name='contactdetail',
            name='icon',
            field=models.CharField(default=b'', help_text=b'a bootstrap icon, f.e. home, bullhorn, envelope, globe, etc.\nSee: http://getbootstrap.com/components/#glyphicons-glyphs', max_length=200, choices=[(b'home', b'Haus'), (b'bullhorn', b'Megaphone'), (b'envelope', b'Umschlag'), (b'globe', b'Weltkugel'), (b'gift', b'Geschenk'), (b'earphone', b'Telefon')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='knowledgelevel',
            name='icon',
            field=models.CharField(default=b'', help_text=b'a bootstrap icon, f.e. home, bullhorn, envelope, globe, etc.\nSee: http://getbootstrap.com/components/#glyphicons-glyphs', max_length=200, choices=[(b'home', b'Haus'), (b'bullhorn', b'Megaphone'), (b'envelope', b'Umschlag'), (b'globe', b'Weltkugel'), (b'gift', b'Geschenk'), (b'earphone', b'Telefon')]),
            preserve_default=True,
        ),
    ]
