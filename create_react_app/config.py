import re

from django.conf import settings
from importlib import import_module

__all__ = ('load_config',)

_loaders = {}
ASSET_LOADER_CACHE = getattr(settings, "RUNTIME_ASSET_LOADER", False)

DEFAULT_CONFIG = {
    'DEFAULT': {
        'CACHE': True,
        'BUNDLE_DIR_NAME': '/Users/aamirbhatt/workspace/hack_django_react/dashboard/static',
        'LOADER_CLASS': 'create_react_app.loader.CreateReactLoader',
        'FRONT_END_SERVER': "http://localhost:3000/",
        'PUBLIC_PATH': "static/",
        "PUBLIC_PATH_DEV": "/",
        'IS_DEV': False
    }
}

user_config = getattr(settings, 'CREATE_REACT_APP', DEFAULT_CONFIG)

user_config = dict(
    (name, dict(DEFAULT_CONFIG['DEFAULT'], **cfg))
    for name, cfg in user_config.items()
)


def load_config(name):
    return user_config[name]


def import_string(dotted_path):
    '''
    This is a rough copy of django's import_string, which wasn't introduced until Django 1.7
    Once this package's support for Django 1.6 has been removed, this can be safely replaced with
    `from django.utils.module_loading import import_string`
    '''
    try:
        module_path, class_name = dotted_path.rsplit('.', 1)
        module = import_module(module_path)
        return getattr(module, class_name)
    except (ValueError, AttributeError, ImportError):
        raise ImportError('%s doesn\'t look like a valid module path' % dotted_path)


def get_loader(config_name, manifest_path=None):
    if config_name not in _loaders or ASSET_LOADER_CACHE:
        config = load_config(config_name)
        loader_class = import_string(config['LOADER_CLASS'])
        _loaders[config_name] = loader_class(config, manifest_path)
    return _loaders[config_name]
