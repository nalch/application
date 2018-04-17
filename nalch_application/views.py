from django.http import HttpResponse
from django.shortcuts import (
    get_object_or_404,
    render_to_response
)
from django.template import RequestContext
# for future use
# from django.template.loader import select_template

from itertools import chain


from nalch_application.models import (
    Applicant,
    Project,
)


def get_shared_context(request, applicant, active='index'):
    """
    collects common information about an applicant and stores them in the context
    Information:
        active -> active page
        applicant -> current applicant
        references -> the applicant's published references
    :param request: HTTPRequest
    :type request: HttpRequest
    :param applicant: the current applicant's name
    :type applicant: str
    :param active: active page, default: index
    :type active: str
    :return: the common context (keys: active, applicant, references)
    :rtype: dict
    """
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
    """
    render index view with common context. Template is application/<applicant.template>/index.html or the default
    application/index.html
    :param request: HTTPRequest
    :type request: HttpRequest
    :param applicant: The current applicant
    :type applicant: str
    :return: rendered template as HttpResponse
    :rtype: HttpResponse
    """
    # for future use:
    #   template = select_template(['application/%s/index.htm' % applicant.template, 'application/index.html'])
    context = get_shared_context(request, applicant)
    return render_to_response(
            'application/%s/index.html' % context['applicant'].template,
            context,
            context_instance=RequestContext(request)
    )


def contact(request, applicant):
    """
    render contact view with common context. Template is application/<applicant.template>/contact.html or the default
    application/contact.html
    :param request: HTTPRequest
    :type request: HttpRequest
    :param applicant: The current applicant
    :type applicant: str
    :return: rendered template as HttpResponse
    :rtype: HttpResponse
    """
    context = get_shared_context(request, applicant, 'contact')
    return render_to_response(
            'application/%s/contact.html' % context['applicant'].template,
            context,
            context_instance=RequestContext(request)
    )


def references(request, applicant, reference):
    """
    render reference view with common context and a current detailed reference.
    Template is application/<applicant.template>/references.html or the default application/references.html
    :param request: HTTPRequest
    :type request: HttpRequest
    :param applicant: The current applicant
    :type applicant: str
    :param reference: The current reference project
    :type reference: Project
    :return: rendered template as HttpResponse
    :rtype: HttpResponse
    """
    context = get_shared_context(request, applicant, 'references')
    current_ref = Project.objects.filter(publish=True, user__user__username=applicant, short_name_en=reference).first()
    if current_ref is None:
        current_ref = Project.objects.filter(publish=True, user__user__username=applicant).first()
    context.update(
        {
            'current_reference': current_ref
        }
    )
    return render_to_response(
        'application/%s/references.html' % context['applicant'].template,
        context,
        context_instance=RequestContext(request)
    )


def areasofinterest(request, applicant):
    """
    render areasofinterest view with common context and the applicant's areas of interest (key: areas).
    Template is application/<applicant.template>/areas.html or the
    default application/areas.html
    :param request: HTTPRequest
    :type request: HttpRequest
    :param applicant: The current applicant
    :type applicant: str
    :return: rendered template as HttpResponse
    :rtype: HttpResponse
    """
    context = get_shared_context(request, applicant, 'areasofinterest')
    context.update(
            {
                'areas': get_object_or_404(Applicant, user__username=applicant).areas_of_interest.all()
            }
    )
    return render_to_response(
            'application/%s/areas.html' % context['applicant'].template,
            context,
            context_instance=RequestContext(request)
    )


def areasofexpertise(request, applicant):
    """
    render areasofexpertise view with common context and the applicant's areas of expertise (key: areas).
    Template is application/<applicant.template>/areas.html or the
    default application/areas.html
    :param request: HTTPRequest
    :type request: HttpRequest
    :param applicant: The current applicant
    :type applicant: str
    :return: rendered template as HttpResponse
    :rtype: HttpResponse
    """
    context = get_shared_context(request, applicant, 'areasofexpertise')
    context.update(
            {
                'areas': get_object_or_404(Applicant, user__username=applicant).areas_of_expertise.all()
            }
    )
    return render_to_response(
            'application/%s/areas.html' % context['applicant'].template,
            context,
            context_instance=RequestContext(request)
    )
