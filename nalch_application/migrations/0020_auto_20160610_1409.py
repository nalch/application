# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nalch_application', '0019_auto_20160602_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactdetail',
            name='icon',
            field=models.CharField(default=b'', help_text=b'a bootstrap or font awesome icon', max_length=200, choices=[(b'earphone', 'earphone'), (b'redhat', 'redhat'), (b'nodejs', 'nodejs'), (b'globe', 'globe'), (b'kibana', 'kibana'), (b'travis', 'travis'), (b'angularjs', 'angularjs'), (b'linux', 'linux'), (b'home', 'home'), (b'check', 'check'), (b'thumbs-up', 'thumbs-up'), (b'java', 'java'), (b'terminal', 'terminal'), (b'phone-alt', 'phone-alt'), (b'map-marker', 'map-marker'), (b'javascript', 'javascript'), (b'envelope', 'envelope'), (b'nginx', 'nginx'), (b'bullhorn', 'bullhorn'), (b'html5', 'html5'), (b'jquery', 'jquery'), (b'github', 'github'), (b'configurationmanagement', 'configurationmanagement'), (b'gift', 'gift'), (b'phone', 'phone'), (b'mobile', 'mobile'), (b'linkedin', 'linkedin'), (b'elasticsearch', 'elasticsearch'), (b'wrench', 'wrench')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='knowledgelevel',
            name='icon',
            field=models.CharField(default=b'', help_text=b'a bootstrap or font awesome icon', max_length=200, choices=[(b'earphone', 'earphone'), (b'redhat', 'redhat'), (b'nodejs', 'nodejs'), (b'globe', 'globe'), (b'kibana', 'kibana'), (b'travis', 'travis'), (b'angularjs', 'angularjs'), (b'linux', 'linux'), (b'home', 'home'), (b'check', 'check'), (b'thumbs-up', 'thumbs-up'), (b'java', 'java'), (b'terminal', 'terminal'), (b'phone-alt', 'phone-alt'), (b'map-marker', 'map-marker'), (b'javascript', 'javascript'), (b'envelope', 'envelope'), (b'nginx', 'nginx'), (b'bullhorn', 'bullhorn'), (b'html5', 'html5'), (b'jquery', 'jquery'), (b'github', 'github'), (b'configurationmanagement', 'configurationmanagement'), (b'gift', 'gift'), (b'phone', 'phone'), (b'mobile', 'mobile'), (b'linkedin', 'linkedin'), (b'elasticsearch', 'elasticsearch'), (b'wrench', 'wrench')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tag',
            name='icon',
            field=models.CharField(default=b'', help_text=b'a bootstrap or font awesome icon', max_length=200, choices=[(b'earphone', 'earphone'), (b'redhat', 'redhat'), (b'nodejs', 'nodejs'), (b'globe', 'globe'), (b'kibana', 'kibana'), (b'travis', 'travis'), (b'angularjs', 'angularjs'), (b'linux', 'linux'), (b'home', 'home'), (b'check', 'check'), (b'thumbs-up', 'thumbs-up'), (b'java', 'java'), (b'terminal', 'terminal'), (b'phone-alt', 'phone-alt'), (b'map-marker', 'map-marker'), (b'javascript', 'javascript'), (b'envelope', 'envelope'), (b'nginx', 'nginx'), (b'bullhorn', 'bullhorn'), (b'html5', 'html5'), (b'jquery', 'jquery'), (b'github', 'github'), (b'configurationmanagement', 'configurationmanagement'), (b'gift', 'gift'), (b'phone', 'phone'), (b'mobile', 'mobile'), (b'linkedin', 'linkedin'), (b'elasticsearch', 'elasticsearch'), (b'wrench', 'wrench')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='technology',
            name='icon',
            field=models.CharField(default=b'', help_text=b'a bootstrap or font awesome icon', max_length=200, choices=[(b'earphone', 'earphone'), (b'redhat', 'redhat'), (b'nodejs', 'nodejs'), (b'globe', 'globe'), (b'kibana', 'kibana'), (b'travis', 'travis'), (b'angularjs', 'angularjs'), (b'linux', 'linux'), (b'home', 'home'), (b'check', 'check'), (b'thumbs-up', 'thumbs-up'), (b'java', 'java'), (b'terminal', 'terminal'), (b'phone-alt', 'phone-alt'), (b'map-marker', 'map-marker'), (b'javascript', 'javascript'), (b'envelope', 'envelope'), (b'nginx', 'nginx'), (b'bullhorn', 'bullhorn'), (b'html5', 'html5'), (b'jquery', 'jquery'), (b'github', 'github'), (b'configurationmanagement', 'configurationmanagement'), (b'gift', 'gift'), (b'phone', 'phone'), (b'mobile', 'mobile'), (b'linkedin', 'linkedin'), (b'elasticsearch', 'elasticsearch'), (b'wrench', 'wrench')]),
            preserve_default=True,
        ),
    ]
