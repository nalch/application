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
                ('icon', models.CharField(default=b'', help_text=b'a bootstrap icon, f.e. home, bullhorn, envelope, globe, etc.\nSee: http://getbootstrap.com/components/#glyphicons-glyphs', max_length=200, choices=[(b'home', 'home'), (b'bullhorn', 'bullhorn'), (b'envelope', 'envelope'), (b'globe', 'globe'), (b'gift', 'gift'), (b'earphone', 'earphone'), (b'thumbs-up', 'thumbs-up'), (b'check', 'check'), (b'wrench', 'wrench')])),
                ('applicant', models.ForeignKey(blank=True, to='nalch_application.Applicant', null=True)),
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
                ('project', models.ForeignKey(to='nalch_application.Project')),
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
            field=models.ManyToManyField(to='nalch_application.Group'),
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
    ]
