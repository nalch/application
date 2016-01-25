from modeltranslation.translator import (
    translator,
    TranslationOptions
)

from .models import (
    Applicant,
    ContactDetail,
    Project,
    ProjectImage
)


class ApplicantTranslationOptions(TranslationOptions):
    fields = ('address',)


class ContactDetailTranslationOptions(TranslationOptions):
    fields = ('text',)


class ProjectTranslationOptions(TranslationOptions):
    fields = ('name', 'short_name', 'description',)


class ProjectImageTranslationOptions(TranslationOptions):
    fields = ('title',)

translator.register(Applicant, ApplicantTranslationOptions)
translator.register(ContactDetail, ContactDetailTranslationOptions)
translator.register(Project, ProjectTranslationOptions)
translator.register(ProjectImage, ProjectImageTranslationOptions)
