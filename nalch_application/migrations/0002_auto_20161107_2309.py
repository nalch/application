# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import colorful.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nalch_application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('birthday', models.DateField(null=True, blank=True)),
                ('address', models.TextField(null=True, blank=True)),
                ('address_de', models.TextField(null=True, blank=True)),
                ('address_en', models.TextField(null=True, blank=True)),
                ('profile_picture', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('template', models.CharField(default=b'photon', max_length=250, null=True, blank=True, choices=[(b'photon', 'photon')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AreaOfInterest',
            fields=[
                ('name_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('name_de', models.CharField(max_length=200, unique=True, null=True)),
                ('name_en', models.CharField(max_length=200, unique=True, null=True)),
                ('description', models.TextField()),
                ('description_de', models.TextField(null=True)),
                ('description_en', models.TextField(null=True)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AreaOfKnowledge',
            fields=[
                ('name_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('name_de', models.CharField(max_length=200, unique=True, null=True)),
                ('name_en', models.CharField(max_length=200, unique=True, null=True)),
                ('description', models.TextField()),
                ('description_de', models.TextField(null=True)),
                ('description_en', models.TextField(null=True)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('name_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('name_de', models.CharField(max_length=200, unique=True, null=True)),
                ('name_en', models.CharField(max_length=200, unique=True, null=True)),
                ('file', models.FileField(upload_to=b'')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContactDetail',
            fields=[
                ('name_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('name_de', models.CharField(max_length=200, unique=True, null=True)),
                ('name_en', models.CharField(max_length=200, unique=True, null=True)),
                ('icon', models.CharField(default=b'', help_text=b'a bootstrap or font awesome icon', max_length=200, choices=[(b'earphone', 'earphone'), (b'redhat', 'redhat'), (b'nodejs', 'nodejs'), (b'globe', 'globe'), (b'kibana', 'kibana'), (b'travis', 'travis'), (b'angularjs', 'angularjs'), (b'linux', 'linux'), (b'home', 'home'), (b'check', 'check'), (b'thumbs-up', 'thumbs-up'), (b'java', 'java'), (b'terminal', 'terminal'), (b'phone-alt', 'phone-alt'), (b'map-marker', 'map-marker'), (b'javascript', 'javascript'), (b'envelope', 'envelope'), (b'nginx', 'nginx'), (b'bullhorn', 'bullhorn'), (b'html5', 'html5'), (b'jquery', 'jquery'), (b'github', 'github'), (b'configurationmanagement', 'configurationmanagement'), (b'gift', 'gift'), (b'phone', 'phone'), (b'mobile', 'mobile'), (b'linkedin', 'linkedin'), (b'elasticsearch', 'elasticsearch'), (b'wrench', 'wrench')])),
                ('link', models.BooleanField(default=False)),
                ('applicant', models.ForeignKey(blank=True, to='nalch_application.Applicant', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('icon', models.CharField(default=b'', help_text=b'a bootstrap or font awesome icon', max_length=200, choices=[(b'earphone', 'earphone'), (b'redhat', 'redhat'), (b'nodejs', 'nodejs'), (b'globe', 'globe'), (b'kibana', 'kibana'), (b'travis', 'travis'), (b'angularjs', 'angularjs'), (b'linux', 'linux'), (b'home', 'home'), (b'check', 'check'), (b'thumbs-up', 'thumbs-up'), (b'java', 'java'), (b'terminal', 'terminal'), (b'phone-alt', 'phone-alt'), (b'map-marker', 'map-marker'), (b'javascript', 'javascript'), (b'envelope', 'envelope'), (b'nginx', 'nginx'), (b'bullhorn', 'bullhorn'), (b'html5', 'html5'), (b'jquery', 'jquery'), (b'github', 'github'), (b'configurationmanagement', 'configurationmanagement'), (b'gift', 'gift'), (b'phone', 'phone'), (b'mobile', 'mobile'), (b'linkedin', 'linkedin'), (b'elasticsearch', 'elasticsearch'), (b'wrench', 'wrench')])),
                ('description', models.TextField()),
                ('description_de', models.TextField(null=True)),
                ('description_en', models.TextField(null=True)),
                ('user', models.OneToOneField(to='nalch_application.Applicant')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('name_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('name_de', models.CharField(max_length=200, unique=True, null=True)),
                ('name_en', models.CharField(max_length=200, unique=True, null=True)),
                ('description', models.TextField()),
                ('description_de', models.TextField(null=True)),
                ('description_en', models.TextField(null=True)),
                ('short_name', models.CharField(unique=True, max_length=25)),
                ('short_name_de', models.CharField(max_length=25, unique=True, null=True)),
                ('short_name_en', models.CharField(max_length=25, unique=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='KnowledgeLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('icon', models.CharField(default=b'', help_text=b'a bootstrap or font awesome icon', max_length=200, choices=[(b'earphone', 'earphone'), (b'redhat', 'redhat'), (b'nodejs', 'nodejs'), (b'globe', 'globe'), (b'kibana', 'kibana'), (b'travis', 'travis'), (b'angularjs', 'angularjs'), (b'linux', 'linux'), (b'home', 'home'), (b'check', 'check'), (b'thumbs-up', 'thumbs-up'), (b'java', 'java'), (b'terminal', 'terminal'), (b'phone-alt', 'phone-alt'), (b'map-marker', 'map-marker'), (b'javascript', 'javascript'), (b'envelope', 'envelope'), (b'nginx', 'nginx'), (b'bullhorn', 'bullhorn'), (b'html5', 'html5'), (b'jquery', 'jquery'), (b'github', 'github'), (b'configurationmanagement', 'configurationmanagement'), (b'gift', 'gift'), (b'phone', 'phone'), (b'mobile', 'mobile'), (b'linkedin', 'linkedin'), (b'elasticsearch', 'elasticsearch'), (b'wrench', 'wrench')])),
                ('weight', models.CharField(default=b'', max_length=200, choices=[(b'basic', 'basic knowledge'), (b'working', 'working knowledge'), (b'advanced', 'advanced knowledge')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('name_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('name_de', models.CharField(max_length=200, unique=True, null=True)),
                ('name_en', models.CharField(max_length=200, unique=True, null=True)),
                ('short_name', models.CharField(unique=True, max_length=25)),
                ('short_name_de', models.CharField(max_length=25, unique=True, null=True)),
                ('short_name_en', models.CharField(max_length=25, unique=True, null=True)),
                ('description', models.TextField()),
                ('description_de', models.TextField(null=True)),
                ('description_en', models.TextField(null=True)),
                ('title_thumbnail', models.ImageField(upload_to=b'')),
                ('publish', models.BooleanField(default=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('groups', models.ManyToManyField(to='nalch_application.Group')),
            ],
            options={
                'ordering': ('order',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('name_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('name_de', models.CharField(max_length=200, unique=True, null=True)),
                ('name_en', models.CharField(max_length=200, unique=True, null=True)),
                ('image', models.ImageField(upload_to=b'')),
                ('thumbnail', models.ImageField(upload_to=b'')),
                ('project', models.ForeignKey(related_name='images', to='nalch_application.Project')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('name_de', models.CharField(max_length=200, unique=True, null=True)),
                ('name_en', models.CharField(max_length=200, unique=True, null=True)),
                ('icon', models.CharField(default=b'', help_text=b'a bootstrap or font awesome icon', max_length=200, choices=[(b'earphone', 'earphone'), (b'redhat', 'redhat'), (b'nodejs', 'nodejs'), (b'globe', 'globe'), (b'kibana', 'kibana'), (b'travis', 'travis'), (b'angularjs', 'angularjs'), (b'linux', 'linux'), (b'home', 'home'), (b'check', 'check'), (b'thumbs-up', 'thumbs-up'), (b'java', 'java'), (b'terminal', 'terminal'), (b'phone-alt', 'phone-alt'), (b'map-marker', 'map-marker'), (b'javascript', 'javascript'), (b'envelope', 'envelope'), (b'nginx', 'nginx'), (b'bullhorn', 'bullhorn'), (b'html5', 'html5'), (b'jquery', 'jquery'), (b'github', 'github'), (b'configurationmanagement', 'configurationmanagement'), (b'gift', 'gift'), (b'phone', 'phone'), (b'mobile', 'mobile'), (b'linkedin', 'linkedin'), (b'elasticsearch', 'elasticsearch'), (b'wrench', 'wrench')])),
                ('color', colorful.fields.RGBColorField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('name_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('name_de', models.CharField(max_length=200, unique=True, null=True)),
                ('name_en', models.CharField(max_length=200, unique=True, null=True)),
                ('icon', models.CharField(default=b'', help_text=b'a bootstrap or font awesome icon', max_length=200, choices=[(b'earphone', 'earphone'), (b'redhat', 'redhat'), (b'nodejs', 'nodejs'), (b'globe', 'globe'), (b'kibana', 'kibana'), (b'travis', 'travis'), (b'angularjs', 'angularjs'), (b'linux', 'linux'), (b'home', 'home'), (b'check', 'check'), (b'thumbs-up', 'thumbs-up'), (b'java', 'java'), (b'terminal', 'terminal'), (b'phone-alt', 'phone-alt'), (b'map-marker', 'map-marker'), (b'javascript', 'javascript'), (b'envelope', 'envelope'), (b'nginx', 'nginx'), (b'bullhorn', 'bullhorn'), (b'html5', 'html5'), (b'jquery', 'jquery'), (b'github', 'github'), (b'configurationmanagement', 'configurationmanagement'), (b'gift', 'gift'), (b'phone', 'phone'), (b'mobile', 'mobile'), (b'linkedin', 'linkedin'), (b'elasticsearch', 'elasticsearch'), (b'wrench', 'wrench')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WeightedTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project', models.ForeignKey(blank=True, to='nalch_application.Project', null=True)),
                ('tag', models.ForeignKey(to='nalch_application.Tag')),
                ('weight', models.ForeignKey(to='nalch_application.KnowledgeLevel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='project',
            name='technologies',
            field=models.ManyToManyField(to='nalch_application.Technology', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(to='nalch_application.Applicant'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attachment',
            name='project',
            field=models.ForeignKey(to='nalch_application.Project'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='areaofknowledge',
            name='tags',
            field=models.ManyToManyField(to='nalch_application.Tag', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='areaofknowledge',
            name='technologies',
            field=models.ManyToManyField(to='nalch_application.Technology', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='areaofinterest',
            name='tags',
            field=models.ManyToManyField(to='nalch_application.Tag', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='areaofinterest',
            name='technologies',
            field=models.ManyToManyField(to='nalch_application.Technology', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='applicant',
            name='areas_of_expertise',
            field=models.ManyToManyField(related_name='expertises', null=True, to='nalch_application.AreaOfKnowledge', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='applicant',
            name='areas_of_interest',
            field=models.ManyToManyField(related_name='interests', null=True, to='nalch_application.AreaOfInterest', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='applicant',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
