from django.contrib import admin

from modeltranslation.admin import (
    TranslationAdmin,
    TranslationTabularInline
)

from .models import (
    Applicant,
    Attachment,
    ContactDetail,
    Project,
    ProjectImage,
    Tag,
)


class ContactDetailInline(admin.TabularInline):
    exclude = ('text', )
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


class ProjectAdmin(TranslationAdmin):
    inlines = [ProjectImageInline, AttachmentInline, ]


admin.site.register(Tag, TagAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Applicant, ApplicantAdmin)

