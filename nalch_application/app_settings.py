from django.conf import settings


ICONS = getattr(settings, 'NALCH_APPLICATION_ICONS', [
    'home',
    'bullhorn',
    'envelope',
    'globe',
    'gift',
    'phone-alt',
    'earphone',
    'thumbs-up',
    'check',
    'wrench',
])
