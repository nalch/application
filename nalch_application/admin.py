from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from .models import (
    Applicant,
    ContactDetail,
    Project
)


class ApplicantAdmin(TranslationAdmin):
    pass


class ContactDetailAdmin(TranslationAdmin):
    pass


class ProjectAdmin(TranslationAdmin):
    pass

admin.site.register(Project, ProjectAdmin)
admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(ContactDetail, ContactDetailAdmin)
