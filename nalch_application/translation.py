from modeltranslation.translator import (
    translator,
    TranslationOptions
)

from .models import (
    Applicant,
    AreaOfInterest,
    AreaOfKnowledge,
    Attachment,
    ContactDetail,
    Description,
    Group,
    Project,
    ProjectImage,
    Tag,
    Technology,
    TranslatableNameMixin,
)


class TNMTranslationOptions(TranslationOptions):
    fields = ('name', )


class ApplicantTranslationOptions(TranslationOptions):
    fields = ('address', )


class DescriptionTranslationOptions(TranslationOptions):
    fields = ('description', )


class ContactDetailTranslationOptions(TNMTranslationOptions):
    pass


class ProjectTranslationOptions(TNMTranslationOptions):
    fields = ('description', 'short_description', 'short_name', )


class ProjectImageTranslationOptions(TNMTranslationOptions):
    pass


class AttachmentTranslationOptions(TNMTranslationOptions):
    pass


class TagTranslationOptions(TNMTranslationOptions):
    pass


class TechnologyTranslationOptions(TNMTranslationOptions):
    pass


class GroupTranslationOptions(TNMTranslationOptions):
    fields = ('description', 'short_name', )


class AreaMixinTranslationOptions(TNMTranslationOptions):
    fields = ('description', )


translator.register(TranslatableNameMixin, TNMTranslationOptions)
translator.register(Applicant, ApplicantTranslationOptions)
translator.register(ContactDetail, ContactDetailTranslationOptions)
translator.register(Description, DescriptionTranslationOptions)
translator.register(Project, ProjectTranslationOptions)
translator.register(ProjectImage, ProjectImageTranslationOptions)
translator.register(Attachment, AttachmentTranslationOptions)
translator.register(Tag, TagTranslationOptions)
translator.register(Technology, TagTranslationOptions)
translator.register(Group, GroupTranslationOptions)
translator.register(AreaOfInterest, AreaMixinTranslationOptions)
translator.register(AreaOfKnowledge, AreaMixinTranslationOptions)
