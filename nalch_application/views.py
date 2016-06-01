from django.http import HttpResponse
from django.shortcuts import (
    get_object_or_404,
    render_to_response
)
from django.template import RequestContext
from django.template.loader import select_template

from itertools import chain


from nalch_application.models import (
    Applicant,
    Project,
)


def get_shared_context(request, applicant, active='index'):
    get_object_or_404(Applicant, user__username=applicant)
    projects = Project.objects.filter(publish=True, user__user__username=applicant)
    # get all groups for all references, flatten the list using itertools and remove duplicates
    groups = set(chain.from_iterable([reference.groups.all() for reference in projects]))
    # group references -> references: { group1: [reference1, reference2, ...], group2: [...], ...}
    references = {
        group: [reference for reference in projects if group in reference.groups.all()] for group in groups
    }
    context = {
        'active': active,
        'applicant': Applicant.objects.get(user__username=applicant),
        'references': references,
    }
    return context


def index(request, applicant):
    # template = select_template(['application/%s/index.htm' % applicant.username, 'application/index.html'])
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


def references(request, applicant, reference):
    context = get_shared_context(request, applicant, 'references')
    current_ref = Project.objects.filter(publish=True, user__user__username=applicant, short_name=reference).first()
    if current_ref is None:
        current_ref = Project.objects.filter(publish=True, user__user__username=applicant).first()
    context.update(
        {
            'current_reference': current_ref
        }
    )
    return render_to_response(
        'application/%s/references.html' % 'photon',
        context,
        context_instance=RequestContext(request)
    )


def areasofinterest(request, applicant):
    context = get_shared_context(request, applicant, 'areasofinterest')
    context.update(
            {
                'areas': get_object_or_404(Applicant, user__username=applicant).areas_of_interest.all()
            }
    )
    return render_to_response(
            'application/areas.html',
            context,
            context_instance=RequestContext(request)
    )


def areasofexpertise(request, applicant):
    context = get_shared_context(request, applicant, 'areasofexpertise')
    context.update(
            {
                'areas': get_object_or_404(Applicant, user__username=applicant).areas_of_expertise.all()
            }
    )
    return render_to_response(
            'application/areas.html',
            context,
            context_instance=RequestContext(request)
    )
