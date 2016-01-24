from modeltranslation.translator import (
    translator,
    TranslationOptions
)

from .models import (
    Applicant,
    ContactDetail,
    Project
)


class ApplicantTranslationOptions(TranslationOptions):
    fields = ('address',)


class ContactDetailTranslationOptions(TranslationOptions):
    fields = ('text',)


class ProjectTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)

translator.register(Applicant, ApplicantTranslationOptions)
translator.register(ContactDetail, ContactDetailTranslationOptions)
translator.register(Project, ProjectTranslationOptions)
