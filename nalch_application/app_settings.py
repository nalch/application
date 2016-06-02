from django.conf import settings


TEMPLATES = getattr(settings, 'NALCH_APPLICATION_TEMPLATES', [
    'photon',
])

ICONS = getattr(settings, 'NALCH_APPLICATION_ICONS', {
    'home': {},
    'bullhorn': {},
    'globe': {
        'fontawesome_css': 'fa-globe',
    },
    'gift': {},
    'phone-alt': {},
    'earphone': {},
    'thumbs-up': {},
    'check': {},
    'wrench': {},
    'phone': {
        'fontawesome_css': 'fa-phone',
    },
    'mobile': {
        'fontawesome_css': 'fa-mobile',
    },
    'map-marker': {},
    'nginx': {
        'devicon_css': 'devicon devicon-nginx-original colored',
    },
    'nodejs': {
        'devicon_css': 'devicon devicon-nodejs-plain-wordmark colored',
    },
    'redhat': {
        'devicon_css': 'devicon devicon-redhat-plain-wordmark colored',
    },
    'linux': {
        'devicon_css': 'devicon devicon-linux-plain',
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
    'elasticsearch': {
        'fontawesome_css': 'fa-search',
    },
})
FONTICONS = filter(lambda icon: 'fontawesome_css' in ICONS[icon] or 'devicon_css' in ICONS[icon], ICONS)
