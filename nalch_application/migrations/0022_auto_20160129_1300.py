# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0021_auto_20160129_1250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('icon', models.CharField(default=b'', help_text=b'a bootstrap icon, f.e. home, bullhorn, envelope, globe, etc.\nSee: http://getbootstrap.com/components/#glyphicons-glyphs', max_length=200, choices=[(b'home', b'Haus'), (b'bullhorn', b'Megaphone'), (b'envelope', b'Umschlag'), (b'globe', b'Weltkugel'), (b'gift', b'Geschenk'), (b'earphone', b'Telefon')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='contactdetail',
            name='icon',
            field=models.ForeignKey(to='nalch_application.Icon'),
            preserve_default=True,
        ),
    ]
