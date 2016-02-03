ALLOWED_HOSTS = [{{ project.allowed_hosts }}]

STATIC_ROOT = {{ project.static_root }}
MEDIA_ROOT = {{ project.media_root }}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': {{ project.database.name }},
    }
}

LOCALE_PATHS = (
    {{ project.locale_path }}
)

SECRET_KEY = {{ project.secret_key }}
DEBUG = False
TEMPLATE_DEBUG = False