# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0005_auto_20160122_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('icon', models.CharField(default=b'', help_text=b'a bootstrap icon, f.e. home, bullhorn, envelope, globe, etc.', max_length=200, choices=[(b'home', b'Haus'), (b'bullhorn', b'Megaphone'), (b'envelope', b'Umschlag'), (b'globe', b'Weltkugel'), (b'gift', b'Geschenk')])),
                ('text', models.TextField(default=b'')),
                ('applicant', models.ForeignKey(to='nalch_application.Applicant')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
