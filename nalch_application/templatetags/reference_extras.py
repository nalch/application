import functools

from django import template
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import render_to_string

from ..app_settings import ICONS

from ..models import (
    Project,
    WeightedTag
)

register = template.Library()


@register.simple_tag
def reference_table(applicant, references):
    """
    render a short table with information of reference projects
    :param applicant: the applicant to get the references for
    :type applicant: Applicant
    :param references: all references
    :type references: lst
    :return: rendered template
    :rtype: str
    """
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
    """
    return an icon denoting a WeightedTag's knowledgelevel
    :param tag: the tag to get the knowledgelevel for
    :type tag: WeightedTag
    :param project: the project for the tag (knowledgelevels/usage is different for the same tag on different projects)
    :type project: Project
    :return: the icon for the tag's knowledgelevel
    :rtype: str
    """
    try:
        return WeightedTag.objects.get(project=project, tag=tag).weight.icon
    except ObjectDoesNotExist:
        return ''


@register.simple_tag
def reference(reference_item, group=None):
    """
    render a detailled reference
    :param reference_item: the project to render
    :type reference_item: Project
    :return: rendered template as string
    :rtype: str
    """
    context_dict = {
        'group': group,
        'reference': reference_item,
    }
    return render_to_string('application/templatetags/reference.html', context_dict)


@register.simple_tag
def small_reference(reference_item):
    """
    render a reference's overview
    :param reference_item: the project to render
    :type reference_item: Project
    :return: rendered template as string
    :rtype: str
    """
    context_dict = {
        'reference': reference_item,
    }
    return render_to_string('application/templatetags/small_reference.html', context_dict)


@register.simple_tag
def icon_css(iconmixin):
    """

    :param iconmixin:
    :return:
        key missing -> iconmixin
        'icon': {} -> 'icon'
        'icon': {'devicon_css': 'devicon_class someother'} -> 'devicon_class someother'
        'icon': {'fontawesome_css': 'fontawesome', 'devicon_css': 'devicon_class someother'}
            -> 'devicon_class someother'
        'icon': {'fontawesome_css': 'fontawesome'} -> 'fontawesome'
    """
    if iconmixin.icon in ICONS:
        icon = ICONS[iconmixin.icon]
        if 'devicons_css' in icon:
            return icon['devicons_css']
        if 'devicon_css' in icon:
            return icon['devicon_css']
        if 'fontawesome_css' in icon:
            return icon['fontawesome_css']
        return iconmixin.icon
    return iconmixin


@register.filter
def sort(lst, key_name):
    """
    sort a list after a freely chosen key. Similar to the dictsort templatetag but adding recursive keys.
    f.e. myset.all|sort:"nested.keys"
    :param lst: the list to be sorted
    :type lst: lst
    :param key_name: string denoting the sort key
    :type key_name: str
    :return: sorted list
    :rtype: list
    """
    return sorted(
            lst,
            key=lambda item: functools.reduce(
                    lambda obj, key: getattr(obj, key),
                    [item] + key_name.split('.')
            )
    )
