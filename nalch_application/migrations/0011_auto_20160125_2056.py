# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0010_auto_20160124_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'')),
                ('thumbnail', models.ImageField(upload_to=b'')),
                ('project', models.ForeignKey(related_name='images', to='nalch_application.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='contactdetail',
            name='icon',
            field=models.CharField(default=b'', help_text=b'a bootstrap icon, f.e. home, bullhorn, envelope, globe, etc.\nSee: http://getbootstrap.com/components/#glyphicons-glyphs', max_length=200, choices=[(b'home', b'Haus'), (b'bullhorn', b'Megaphone'), (b'envelope', b'Umschlag'), (b'globe', b'Weltkugel'), (b'gift', b'Geschenk'), (b'earphone', b'Telefon')]),
            preserve_default=True,
        ),
    ]
