from django.shortcuts import render_to_response
from django.template import RequestContext

from nalch_application.models import (
    Applicant,
    Group,
    KnowledgeLevel,
    Project,
    WeightedTag,
)


def get_shared_context(request, applicant, active='index'):
    context = {
        'active': active,
        'applicant': Applicant.objects.get(user__username=applicant),
        'references': Project.objects.filter(publish=True, user__user__username=applicant),
    }
    return context


def index(request, applicant):
    return render_to_response(
            'application/index.html',
            get_shared_context(request, applicant),
            context_instance=RequestContext(request)
    )


def contact(request, applicant):
    return render_to_response(
            'application/contact.html',
            get_shared_context(request, applicant, 'contact'),
            context_instance=RequestContext(request)
    )


def references(request, applicant):
    projects = Project.objects.filter(publish=True, user__user__username=applicant)
    groups = Group.objects.filter(project__in=projects)
    weighted_tags = WeightedTag.objects.filter(project__in=projects)
    knowledge_level = set([wt.weight for wt in weighted_tags])
    context = {
        'weighted_tags': weighted_tags,
        'knowledge_level': knowledge_level,
        'groups': groups,
    }.copy()
    context.update(get_shared_context(request, applicant, 'references'))
    return render_to_response(
            'application/references.html',
            context,
            context_instance=RequestContext(request)
    )
