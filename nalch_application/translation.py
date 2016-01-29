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
    TranslatableNameMixin,
)


class TNMTranslationOptions(TranslationOptions):
    fields = ('name', )


class ApplicantTranslationOptions(TranslationOptions):
    fields = ('address',)


class ContactDetailTranslationOptions(TNMTranslationOptions):
    pass


class ProjectTranslationOptions(TNMTranslationOptions):
    fields = ('short_name', 'description', )


class ProjectImageTranslationOptions(TNMTranslationOptions):
    pass


class AttachmentTranslationOptions(TNMTranslationOptions):
    pass


class TagTranslationOptions(TNMTranslationOptions):
    pass


translator.register(TranslatableNameMixin, TNMTranslationOptions)
translator.register(Applicant, ApplicantTranslationOptions)
translator.register(ContactDetail, ContactDetailTranslationOptions)
translator.register(Project, ProjectTranslationOptions)
translator.register(ProjectImage, ProjectImageTranslationOptions)
translator.register(Attachment, AttachmentTranslationOptions)
translator.register(Tag, TagTranslationOptions)
