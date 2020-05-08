from importlib import import_module
from django.conf import settings
from .config import load_config

_loaders = {}


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


def get_loader(config_name):
    if config_name not in _loaders:
        config = load_config(config_name)
        loader_class = import_string(config['LOADER_CLASS'])
        _loaders[config_name] = loader_class(config)
    return _loaders[config_name]


def _filter_by_extension(bundle, extension):
    '''Return only files with the given extension'''
    for chunk in bundle:
        if chunk.endswith('.{0}'.format(extension)):
            yield chunk


def _get_bundle(extension, loader):
    bundle = loader.get_bundle()
    if extension:
        bundle = _filter_by_extension(bundle, extension)
    return bundle


def get_as_tags(extension=None, config='DEFAULT', attrs=''):
    loader = get_loader(config)
    bundle = _get_bundle(extension, loader)
    asset_path = loader.asset_path
    tags = []
    for chunk in bundle:
        if chunk.endswith(('.js', '.js.gz')):
            tags.append((
                            '<script type="text/javascript" src="{0}{1}" {2}></script>'
                        ).format(asset_path, chunk, attrs))
        elif chunk.endswith(('.css', '.css.gz')):
            tags.append((
                            '<link type="text/css" href="{0}{1}" rel="stylesheet" {2}/>'
                        ).format(asset_path, chunk, attrs))
    print(tags, "tags")
    return tags
