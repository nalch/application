from django.conf import settings


TEMPLATES = getattr(settings, 'NALCH_APPLICATION_TEMPLATES', [
    'photon',
])

ICONS = getattr(settings, 'NALCH_APPLICATION_ICONS', {
    'home': {},
    'bullhorn': {},
    'globe': {},
    'gift': {},
    'phone-alt': {},
    'earphone': {},
    'thumbs-up': {},
    'check': {},
    'wrench': {},
    'phone': {},
    'mobile': {},
    'map-marker': {},
    'nginx': {
        'devicon_css': 'devicon devicon-nginx-original colored',
    },
    'nodejs': {
        'devicon_css': 'devicon devicon-nodejs-plain-wordmark colored',
    },
    'kibana': {
        'fontawesome_css': 'style2 fa-area-chart',
    },
    'configurationmanagement': {
        'fontawesome_css': 'style3 fa-cogs',
    },
    'github': {
        'fontawesome_css': 'fa-github',
    },
    'linkedin': {
        'fontawesome_css': 'fa-linkedin-square',
    },
    'envelope': {
        'fontawesome_css': 'fa-envelope',
    },
})
