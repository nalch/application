from adminsortable2.admin import SortableAdminMixin

from django.contrib import admin

from modeltranslation.admin import (
    TranslationAdmin,
    TranslationTabularInline
)

from .models import (
    Applicant,
    AreaOfInterest,
    AreaOfKnowledge,
    Attachment,
    ContactDetail,
    Description,
    Group,
    KnowledgeLevel,
    Project,
    ProjectImage,
    Tag,
    Technology,
    WeightedTag,
)


class DescriptionInline(TranslationTabularInline):
    model = Description


class ContactDetailInline(TranslationTabularInline):
    model = ContactDetail
    extra = 0


class ApplicantAdmin(TranslationAdmin):
    inlines = [DescriptionInline, ContactDetailInline, ]


class ContactDetailAdmin(TranslationAdmin):
    pass


class ProjectImageInline(TranslationTabularInline):
    model = ProjectImage
    extra = 0


class AttachmentInline(TranslationTabularInline):
    model = Attachment
    extra = 0


class TagInline(TranslationTabularInline):
    model = Tag
    extra = 0


class TagAdmin(TranslationAdmin):
    pass


class TechnologyAdmin(TranslationAdmin):
    pass


class GroupAdmin(TranslationAdmin):
    pass


class KnowledgeLevelAdmin(admin.ModelAdmin):
    model = KnowledgeLevel
    extra = 0


class WeightedTagInline(admin.TabularInline):
    model = WeightedTag
    extra = 0


class ProjectAdmin(SortableAdminMixin, TranslationAdmin):
    inlines = [WeightedTagInline, ProjectImageInline, AttachmentInline, ]
    list_display = ('short_name', 'name', 'publish', 'user')


class AreaOfKnowledgeAdmin(SortableAdminMixin, TranslationAdmin):
    pass


class AreaOfInterestAdmin(SortableAdminMixin, TranslationAdmin):
    pass


admin.site.register(Tag, TagAdmin)
admin.site.register(Technology, TechnologyAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(KnowledgeLevel, KnowledgeLevelAdmin)
admin.site.register(AreaOfInterest, AreaOfInterestAdmin)
admin.site.register(AreaOfKnowledge, AreaOfKnowledgeAdmin)
