import re

from django.conf import settings

__all__ = ('load_config',)

DEFAULT_CONFIG = {
    'DEFAULT': {
        'CACHE': True,
        'BUNDLE_DIR_NAME': '/Users/aamirbhatt/workspace/hack_django_react/dashboard/static',
        'LOADER_CLASS': 'create_react_app.loader.CreateReactLoader',
        'FRONT_END_SERVER': "http://localhost:3000/",
        'is_dev': False,
    }
}

user_config = getattr(settings, 'CREATE_REACT_APP', DEFAULT_CONFIG)

user_config = dict(
    (name, dict(DEFAULT_CONFIG['DEFAULT'], **cfg))
    for name, cfg in user_config.items()
)


def load_config(name):
    return user_config[name]
