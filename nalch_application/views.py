from django.shortcuts import render_to_response
from django.template import RequestContext

from nalch_application.models import (
    Applicant,
    Project
)


def get_shared_context(request, applicant, active='index'):
    context = {
        'active': active,
        'applicant': Applicant.objects.get(user__username=applicant),
        'references': Project.objects.filter(publish=True, user__username=applicant),
    }
    return context


def index(request, applicant):
    return render_to_response('application/index.html', get_shared_context(request, applicant))


def contact(request, applicant):
    return render_to_response('application/contact.html', get_shared_context(request, applicant, 'contact'), context_instance=RequestContext(request))


def references(request, applicant):
    return render_to_response('application/references.html', get_shared_context(request, applicant, 'references'))
