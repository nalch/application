from django.shortcuts import (
    get_object_or_404,
    render_to_response
)
from django.template import RequestContext

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


def references(request, applicant):
    context = get_shared_context(request, applicant, 'references')
    return render_to_response(
            'application/references.html',
            context,
            context_instance=RequestContext(request)
    )


def areasofinterest(request, applicant):
    return render_to_response(
            'application/interestareas.html',
            get_shared_context(request, applicant, 'areasofinterest'),
            context_instance=RequestContext(request)
    )
