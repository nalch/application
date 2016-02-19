from django import template
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import render_to_string

from ..models import (
    Project,
    WeightedTag
)

register = template.Library()


@register.simple_tag
def reference_table(applicant, references):
    projects = Project.objects.filter(publish=True, user__user__username=applicant)
    tags = WeightedTag.objects.filter(project__in=projects)
    context_dict = {
        'references': references,
        'tags': set([tag.tag for tag in tags]),
        'knowledge_level': set([wt.weight for wt in WeightedTag.objects.filter(project__in=projects)])
    }
    return render_to_string('application/templatetags/reference_table.html', context_dict)


@register.simple_tag
def knowledge_level(tag, project):
    try:
        return WeightedTag.objects.get(project=project, tag=tag).weight.icon
    except ObjectDoesNotExist:
        return ''


@register.simple_tag
def reference(reference_item, group=None):
    context_dict = {
        'group': group,
        'reference': reference_item,
    }
    return render_to_string('application/templatetags/reference.html', context_dict)


@register.simple_tag
def small_reference(reference_item):
    context_dict = {
        'reference': reference_item,
    }
    return render_to_string('application/templatetags/small_reference.html', context_dict)
