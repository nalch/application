# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import colorful.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('started', models.DateField(null=True, verbose_name=b'date started', blank=True)),
                ('ended', models.DateField(null=True, verbose_name=b'date ended', blank=True)),
                ('title_thumbnail', models.ImageField(upload_to=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('birthday', models.DateField(null=True, blank=True)),
                ('address', models.TextField(null=True, blank=True)),
                ('address_de', models.TextField(null=True, blank=True)),
                ('address_en', models.TextField(null=True, blank=True)),
                ('profile_picture', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
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
                ('project', models.ForeignKey(to='nalch_application.Project')),
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
                ('applicant', models.ForeignKey(blank=True, to='nalch_application.Applicant', null=True)),
                ('link', models.BooleanField(default=False)),
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
                ('icon', models.CharField(default=b'', help_text=b'a bootstrap icon, f.e. home, bullhorn, envelope, globe, etc.\nSee: http://getbootstrap.com/components/#glyphicons-glyphs', max_length=200, choices=[(b'home', 'home'), (b'bullhorn', 'bullhorn'), (b'envelope', 'envelope'), (b'globe', 'globe'), (b'gift', 'gift'), (b'earphone', 'earphone'), (b'thumbs-up', 'thumbs-up'), (b'check', 'check'), (b'wrench', 'wrench')])),
                ('weight', models.CharField(default=b'', max_length=200, choices=[(b'basic', 'basic knowledge'), (b'working', 'working knowledge'), (b'advanced', 'advanced knowledge')])),
            ],
            options={
                'abstract': False,
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
                ('color', colorful.fields.RGBColorField()),
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
        migrations.RemoveField(
            model_name='project',
            name='ended',
        ),
        migrations.RemoveField(
            model_name='project',
            name='id',
        ),
        migrations.RemoveField(
            model_name='project',
            name='started',
        ),
        migrations.AddField(
            model_name='project',
            name='description_de',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='description_en',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='groups',
            field=models.ManyToManyField(to=b'nalch_application.Group'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='name_de',
            field=models.CharField(max_length=200, unique=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='name_en',
            field=models.CharField(max_length=200, unique=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='name_id',
            field=models.AutoField(default=1, serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='publish',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='short_name',
            field=models.CharField(default='', unique=True, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='short_name_de',
            field=models.CharField(max_length=25, unique=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='short_name_en',
            field=models.CharField(max_length=25, unique=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(default=1, to='nalch_application.Applicant'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(unique=True, max_length=200),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('name_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('name_de', models.CharField(max_length=200, unique=True, null=True)),
                ('name_en', models.CharField(max_length=200, unique=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='project',
            name='technologies',
            field=models.ManyToManyField(to=b'nalch_application.Technology', null=True, blank=True),
            preserve_default=True,
        ),
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
            model_name='knowledgelevel',
            name='icon',
            field=models.CharField(default=b'', help_text=b'a bootstrap icon, f.e. home, bullhorn, envelope, globe, etc.\nSee: http://getbootstrap.com/components/#glyphicons-glyphs', max_length=200, choices=[(b'home', 'home'), (b'bullhorn', 'bullhorn'), (b'envelope', 'envelope'), (b'globe', 'globe'), (b'gift', 'gift'), (b'phone-alt', 'phone-alt'), (b'earphone', 'earphone'), (b'thumbs-up', 'thumbs-up'), (b'check', 'check'), (b'wrench', 'wrench')]),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='AreaOfInterest',
            fields=[
                ('name_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('description', models.TextField()),
                ('order', models.PositiveIntegerField(default=0)),
                ('tags', models.ManyToManyField(to=b'nalch_application.Tag', null=True, blank=True)),
                ('technologies', models.ManyToManyField(to=b'nalch_application.Technology', null=True, blank=True)),
                ('description_de', models.TextField(null=True)),
                ('description_en', models.TextField(null=True)),
                ('name_de', models.CharField(max_length=200, unique=True, null=True)),
                ('name_en', models.CharField(max_length=200, unique=True, null=True)),
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
                ('description', models.TextField()),
                ('order', models.PositiveIntegerField(default=0)),
                ('tags', models.ManyToManyField(to=b'nalch_application.Tag', null=True, blank=True)),
                ('technologies', models.ManyToManyField(to=b'nalch_application.Technology', null=True, blank=True)),
                ('description_de', models.TextField(null=True)),
                ('description_en', models.TextField(null=True)),
                ('name_de', models.CharField(max_length=200, unique=True, null=True)),
                ('name_en', models.CharField(max_length=200, unique=True, null=True)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='applicant',
            name='areas_of_expertise',
            field=models.ManyToManyField(related_name='expertises', null=True, to=b'nalch_application.AreaOfKnowledge', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='applicant',
            name='areas_of_interest',
            field=models.ManyToManyField(related_name='interests', null=True, to=b'nalch_application.AreaOfInterest', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='applicant',
            name='template',
            field=models.CharField(default=b'photon', max_length=250, null=True, blank=True, choices=[(b'photon', 'photon')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tag',
            name='icon',
            field=models.CharField(default=b'', help_text=b'a bootstrap or font awesome icon', max_length=200, choices=[(b'earphone', 'earphone'), (b'redhat', 'redhat'), (b'nodejs', 'nodejs'), (b'globe', 'globe'), (b'kibana', 'kibana'), (b'travis', 'travis'), (b'angularjs', 'angularjs'), (b'linux', 'linux'), (b'home', 'home'), (b'check', 'check'), (b'thumbs-up', 'thumbs-up'), (b'java', 'java'), (b'terminal', 'terminal'), (b'phone-alt', 'phone-alt'), (b'map-marker', 'map-marker'), (b'javascript', 'javascript'), (b'envelope', 'envelope'), (b'nginx', 'nginx'), (b'bullhorn', 'bullhorn'), (b'html5', 'html5'), (b'jquery', 'jquery'), (b'github', 'github'), (b'configurationmanagement', 'configurationmanagement'), (b'gift', 'gift'), (b'phone', 'phone'), (b'mobile', 'mobile'), (b'linkedin', 'linkedin'), (b'elasticsearch', 'elasticsearch'), (b'wrench', 'wrench')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='technology',
            name='icon',
            field=models.CharField(default=b'', help_text=b'a bootstrap or font awesome icon', max_length=200, choices=[(b'earphone', 'earphone'), (b'redhat', 'redhat'), (b'nodejs', 'nodejs'), (b'globe', 'globe'), (b'kibana', 'kibana'), (b'travis', 'travis'), (b'angularjs', 'angularjs'), (b'linux', 'linux'), (b'home', 'home'), (b'check', 'check'), (b'thumbs-up', 'thumbs-up'), (b'java', 'java'), (b'terminal', 'terminal'), (b'phone-alt', 'phone-alt'), (b'map-marker', 'map-marker'), (b'javascript', 'javascript'), (b'envelope', 'envelope'), (b'nginx', 'nginx'), (b'bullhorn', 'bullhorn'), (b'html5', 'html5'), (b'jquery', 'jquery'), (b'github', 'github'), (b'configurationmanagement', 'configurationmanagement'), (b'gift', 'gift'), (b'phone', 'phone'), (b'mobile', 'mobile'), (b'linkedin', 'linkedin'), (b'elasticsearch', 'elasticsearch'), (b'wrench', 'wrench')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='knowledgelevel',
            name='icon',
            field=models.CharField(default=b'', help_text=b'a bootstrap or font awesome icon, f.e. home, bullhorn, envelope, globe, etc.\nSee: http://getbootstrap.com/components/#glyphicons-glyphs', max_length=200, choices=[(b'home', 'home'), (b'bullhorn', 'bullhorn'), (b'envelope', 'envelope'), (b'globe', 'globe'), (b'gift', 'gift'), (b'phone-alt', 'phone-alt'), (b'earphone', 'earphone'), (b'thumbs-up', 'thumbs-up'), (b'check', 'check'), (b'wrench', 'wrench'), (b'phone', 'phone'), (b'mobile', 'mobile'), (b'map-marker', 'map-marker')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='knowledgelevel',
            name='icon',
            field=models.CharField(default=b'', help_text=b'a bootstrap or font awesome icon, f.e. home, bullhorn, envelope, globe, etc.\nSee: http://getbootstrap.com/components/#glyphicons-glyphs', max_length=200, choices=[(b'configurationmanagement', 'configurationmanagement'), (b'thumbs-up', 'thumbs-up'), (b'earphone', 'earphone'), (b'gift', 'gift'), (b'nginx', 'nginx'), (b'mobile', 'mobile'), (b'globe', 'globe'), (b'map-marker', 'map-marker'), (b'envelope', 'envelope'), (b'nodejs', 'nodejs'), (b'phone', 'phone'), (b'kibana', 'kibana'), (b'phone-alt', 'phone-alt'), (b'bullhorn', 'bullhorn'), (b'wrench', 'wrench'), (b'home', 'home'), (b'check', 'check')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='knowledgelevel',
            name='icon',
            field=models.CharField(default=b'', help_text=b'a bootstrap or font awesome icon, f.e. home, bullhorn, envelope, globe, etc.\nSee: http://getbootstrap.com/components/#glyphicons-glyphs', max_length=200, choices=[(b'configurationmanagement', 'configurationmanagement'), (b'thumbs-up', 'thumbs-up'), (b'github', 'github'), (b'earphone', 'earphone'), (b'gift', 'gift'), (b'nginx', 'nginx'), (b'mobile', 'mobile'), (b'globe', 'globe'), (b'map-marker', 'map-marker'), (b'envelope', 'envelope'), (b'nodejs', 'nodejs'), (b'phone', 'phone'), (b'kibana', 'kibana'), (b'phone-alt', 'phone-alt'), (b'bullhorn', 'bullhorn'), (b'wrench', 'wrench'), (b'linkedin', 'linkedin'), (b'home', 'home'), (b'check', 'check')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='knowledgelevel',
            name='icon',
            field=models.CharField(default=b'', help_text=b'a bootstrap or font awesome icon', max_length=200, choices=[(b'earphone', 'earphone'), (b'redhat', 'redhat'), (b'nodejs', 'nodejs'), (b'globe', 'globe'), (b'kibana', 'kibana'), (b'travis', 'travis'), (b'angularjs', 'angularjs'), (b'linux', 'linux'), (b'home', 'home'), (b'check', 'check'), (b'thumbs-up', 'thumbs-up'), (b'java', 'java'), (b'terminal', 'terminal'), (b'phone-alt', 'phone-alt'), (b'map-marker', 'map-marker'), (b'javascript', 'javascript'), (b'envelope', 'envelope'), (b'nginx', 'nginx'), (b'bullhorn', 'bullhorn'), (b'html5', 'html5'), (b'jquery', 'jquery'), (b'github', 'github'), (b'configurationmanagement', 'configurationmanagement'), (b'gift', 'gift'), (b'phone', 'phone'), (b'mobile', 'mobile'), (b'linkedin', 'linkedin'), (b'elasticsearch', 'elasticsearch'), (b'wrench', 'wrench')]),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('icon', models.CharField(default=b'', help_text=b'a bootstrap or font awesome icon', max_length=200, choices=[(b'earphone', 'earphone'), (b'redhat', 'redhat'), (b'nodejs', 'nodejs'), (b'globe', 'globe'), (b'kibana', 'kibana'), (b'travis', 'travis'), (b'angularjs', 'angularjs'), (b'linux', 'linux'), (b'home', 'home'), (b'check', 'check'), (b'thumbs-up', 'thumbs-up'), (b'java', 'java'), (b'terminal', 'terminal'), (b'phone-alt', 'phone-alt'), (b'map-marker', 'map-marker'), (b'javascript', 'javascript'), (b'envelope', 'envelope'), (b'nginx', 'nginx'), (b'bullhorn', 'bullhorn'), (b'html5', 'html5'), (b'jquery', 'jquery'), (b'github', 'github'), (b'configurationmanagement', 'configurationmanagement'), (b'gift', 'gift'), (b'phone', 'phone'), (b'mobile', 'mobile'), (b'linkedin', 'linkedin'), (b'elasticsearch', 'elasticsearch'), (b'wrench', 'wrench')])),
                ('description', models.TextField()),
                ('user', models.OneToOneField(to='nalch_application.Applicant')),
                ('description_de', models.TextField(null=True)),
                ('description_en', models.TextField(null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
