from django.contrib.auth.models import User
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Project(models.Model):
    """
    model to represent projects with names, descriptions, images and tags
    """
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=25)
    description = models.TextField()
    title_thumbnail = models.ImageField()
    publish = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag)

    user = models.ForeignKey(User)

    @property
    def public_name(self):
        return self.short_name_en

    def __unicode__(self):
        """
        return the project's name
        :return: project's name
        :rtype str
        """
        return self.name


class Attachment(models.Model):
    name = models.CharField(max_length=200)
    file = models.FileField()
    project = models.ForeignKey(Project)


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images')
    title = models.CharField(max_length=500)
    image = models.ImageField()
    thumbnail = models.ImageField()


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
            ('gift', 'Geschenk'),
            ('earphone', 'Telefon'),
        ],
        max_length=200,
        help_text='a bootstrap icon, f.e. home, bullhorn, envelope, globe, etc.\nSee: http://getbootstrap.com/components/#glyphicons-glyphs'
    )
    text = models.TextField(default='')
    applicant = models.ForeignKey(Applicant, blank=True, null=True)

    def __unicode__(self):
        return '%s: %s' % (self.applicant, self.text)
