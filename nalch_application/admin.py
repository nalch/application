from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from .models import (
    Applicant,
    ContactDetail,
    Project,
    ProjectImage
)


class ContactDetailInline(admin.TabularInline):
    exclude = ('text', )
    model = ContactDetail
    extra = 0


class ApplicantAdmin(TranslationAdmin):
    inlines = [ContactDetailInline, ]


class ContactDetailAdmin(TranslationAdmin):
    pass


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 0


class ProjectAdmin(TranslationAdmin):
    inlines = [ProjectImageInline, ]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Applicant, ApplicantAdmin)
