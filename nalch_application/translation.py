from modeltranslation.translator import (
    translator,
    TranslationOptions
)

from .models import (
    Applicant,
    Attachment,
    ContactDetail,
    Project,
    ProjectImage,
    Tag,
)


class ApplicantTranslationOptions(TranslationOptions):
    fields = ('address',)


class ContactDetailTranslationOptions(TranslationOptions):
    fields = ('text',)


class ProjectTranslationOptions(TranslationOptions):
    fields = ('name', 'short_name', 'description',)


class ProjectImageTranslationOptions(TranslationOptions):
    fields = ('title',)


class AttachmentTranslationOptions(TranslationOptions):
    fields = ('name',)


class TagTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(Applicant, ApplicantTranslationOptions)
translator.register(ContactDetail, ContactDetailTranslationOptions)
translator.register(Project, ProjectTranslationOptions)
translator.register(ProjectImage, ProjectImageTranslationOptions)
translator.register(Attachment, AttachmentTranslationOptions)
translator.register(Tag, TagTranslationOptions)
