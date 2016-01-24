from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    """
    model to represent projects with names, descriptions, images and tags
    """
    name = models.CharField(max_length=200)
    description = models.TextField()
    started = models.DateField('date started', null=True, blank=True)
    ended = models.DateField('date ended', null=True, blank=True)
    title_thumbnail = models.ImageField()
    publish = models.BooleanField(default=True)

    user = models.ForeignKey(User)

    def __unicode__(self):
        """
        return the project's name
        :return: project's name
        :rtype str
        """
        return self.name


class Applicant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(blank=True, null=True)

    def __unicode__(self):
        return self.user.username


class ContactDetail(models.Model):
    icon = models.CharField(
        default='',
        choices=[
            ('home', 'Haus'),
            ('bullhorn', 'Megaphone'),
            ('envelope', 'Umschlag'),
            ('globe', 'Weltkugel'),
            ('gift', 'Geschenk')
        ],
        max_length=200,
        help_text='a bootstrap icon, f.e. home, bullhorn, envelope, globe, etc.'
    )
    text = models.TextField(default='')
    applicant = models.ForeignKey(Applicant, blank=True, null=True)

    def __unicode__(self):
        return '%s: %s' % (self.applicant, self.text)