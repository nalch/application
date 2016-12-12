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
        'fontawesome_css': 'fa-linux',
    },
    'travis': {
        'devicon_css': 'devicon devicon-travis-plain-wordmark colored',
    },
    'jenkins': {
        'devicons_css': 'devicons devicons-jenkins style1',
    },
    'scrum': {
        'devicons_css': 'devicons devicons-scrum',
    },
    'angularjs': {
        'devicon_css': 'devicon devicon-angularjs-plain-wordmark colored',
    },
    'javascript': {
        'devicon_css': 'devicon devicon-javascript-plain colored',
    },
    'jquery': {
        'devicon_css': 'devicon devicon-jquery-plain-wordmark colored',
    },
    'html5': {
        'devicon_css': 'devicon devicon-html5-plain-wordmark colored',
    },
    'java': {
        'devicon_css': 'devicon devicon-java-plain-wordmark colored',
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
    'terminal': {
        'fontawesome_css': 'fa-terminal',
    },
    'windows': {
        'devicon_css': 'devicon devicon-windows8-original colored',
        'fontawesome_css': 'fa-windows style2',
    },
    'jira': {
        'devicons_css': 'devicons devicons-jira',
    },
    'python': {
        'devicons_css': 'devicons devicons-python',
    },
    'django': {
        'devicon_css': 'devicon devicon-django-plain colored',
    },
    'css3': {
        'devicon_css': 'devicon devicon-css3-plain colored',
    },
    'redis': {
        'devicons_css': 'devicons devicons-redis',
    },
    'postgresql': {
        'devicon_css': 'devicon devicon-postgresql-plain colored',
    },
    'debian': {
        'devicons_css': 'devicons devicons-debian',
    },
    'mongodb': {
        'devicon_css': 'devicon devicon-mongodb-plain-wordmark colored',
    },
    'aws': {
        'devicons_css': 'devicon devicon-amazonwebservices-original colored',
    },
    'docker': {
        'devicon_css': 'devicon devicon-docker-plain colored',
    },
    'openshift': {
        'devicons_css': 'devicons devicons-openshift',
    },
    'google-cloud-platform': {
        'devicons_css': 'devicons devicons-google-cloud-platform',
    },
    'bootstrap': {
        'devicon_css': 'devicon devicon-bootstrap-plain colored',
    },
    'php': {
        'devicon_css': 'devicon devicon-php-plain colored',
    },
})
# filter all icons, that have usable fontawesome or devicon representations
FONTICONS = filter(lambda icon: len(ICONS[icon]) > 0, ICONS)
