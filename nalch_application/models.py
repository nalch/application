from colorful.fields import RGBColorField

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from . import app_settings


class TranslatableNameMixin(models.Model):
    name_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True


class IconMixin(models.Model):
    icon = models.CharField(
        default='',
        choices=[(icon, _(icon)) for icon in app_settings.ICONS],
        max_length=200,
        help_text='a bootstrap icon, f.e. home, bullhorn, envelope, globe, etc.\nSee: http://getbootstrap.com/components/#glyphicons-glyphs'
    )

    class Meta:
        abstract = True


class Tag(TranslatableNameMixin):
    color = RGBColorField()


class Group(TranslatableNameMixin):
    description = models.TextField()
    short_name = models.CharField(max_length=25, unique=True)

    @property
    def public_name(self):
        return self.short_name_en

class Applicant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(blank=True, null=True)

    def __unicode__(self):
        return self.user.username


class Project(TranslatableNameMixin):
    """
    model to represent projects with names, descriptions, images and tags
    """
    short_name = models.CharField(max_length=25, unique=True)
    description = models.TextField()
    title_thumbnail = models.ImageField()
    publish = models.BooleanField(default=True)
    # tags = models.ManyToManyField(Tag)
    groups = models.ManyToManyField(Group)

    user = models.ForeignKey(Applicant)

    @property
    def public_name(self):
        return self.short_name_en


class Attachment(TranslatableNameMixin):
    file = models.FileField()
    project = models.ForeignKey(Project)


class ProjectImage(TranslatableNameMixin):
    project = models.ForeignKey(Project, related_name='images')
    image = models.ImageField()
    thumbnail = models.ImageField()


class ContactDetail(TranslatableNameMixin, IconMixin):
    applicant = models.ForeignKey(Applicant, blank=True, null=True)

    def __unicode__(self):
        return '%s: %s' % (self.applicant, self.text)


class KnowledgeLevel(IconMixin):
    weight = models.CharField(
        default='',
        choices=[
            ('basic', _('basic knowledge')),
            ('working', _('working knowledge')),
            ('advanced', _('advanced knowledge')),
        ],
        max_length=200,
    )

    def __unicode__(self):
        return self.weight


class WeightedTag(models.Model):
    tag = models.ForeignKey(Tag)
    weight = models.ForeignKey(KnowledgeLevel)
    project = models.ForeignKey(Project)

    def __unicode__(self):
        return '%s@%s' % (self.tag.name, self.weight)
