from django.contrib import admin

from modeltranslation.admin import (
    TranslationAdmin,
    TranslationTabularInline
)

from .models import (
    Applicant,
    Attachment,
    ContactDetail,
    Group,
    KnowledgeLevel,
    Project,
    ProjectImage,
    Tag,
    Technology,
    WeightedTag,
)


class ContactDetailInline(TranslationTabularInline):
    model = ContactDetail
    extra = 0


class ApplicantAdmin(TranslationAdmin):
    inlines = [ContactDetailInline, ]


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


class ProjectAdmin(TranslationAdmin):
    inlines = [WeightedTagInline, ProjectImageInline, AttachmentInline, ]
    list_display = ('short_name', 'name', 'publish', 'user')


admin.site.register(Tag, TagAdmin)
admin.site.register(Technology, TechnologyAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(KnowledgeLevel, KnowledgeLevelAdmin)
