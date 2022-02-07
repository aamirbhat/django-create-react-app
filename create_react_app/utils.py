from create_react_app.config import get_loader


def _filter_by_extension(bundle, extension):
    ''' Return only files with the given extension '''
    if isinstance(bundle, list):
        for chunk in bundle:
            if chunk.endswith('.{0}'.format(extension)):
                yield chunk
    else:
        if bundle.endswith('.{0}'.format(extension)):
            yield bundle


def _get_bundle(extension, loader):
    bundle = loader.get_bundle()
    if extension:
        bundle = _filter_by_extension(bundle, extension)
    return bundle


def _page_bundle(extension, loader, page_name):
    bundle = loader.get_pages().get(page_name)
    if extension:
        bundle = _filter_by_extension(bundle, extension)
    return bundle


def src_tags(bundle, asset_path, attrs):
    tags = []
    if not bundle:
        return tags
    for chunk in bundle:
        if chunk.endswith(('.js', '.js.gz')):
            tags.append((
                            '<script type="text/javascript" src="{0}{1}" {2}></script>'
                        ).format(asset_path, chunk, attrs))
        elif chunk.endswith(('.css', '.css.gz')):
            tags.append((
                            '<link type="text/css" href="{0}{1}" rel="stylesheet" {2}/>'
                        ).format(asset_path, chunk, attrs))
    return tags


def script_paths(bundle, asset_path):
    tags = []
    if not bundle:
        return tags
    for chunk in bundle:
        if chunk.endswith(('.js', '.js.gz')):
            file = "{0}{1}".format(asset_path, chunk)
            tags.append(file)
        elif chunk.endswith(('.css', '.css.gz')):
            file = "{0}{1}".format(asset_path, chunk)
            tags.append(file)
    return tags


def get_as_tags(extension=None, config='DEFAULT', attrs=''):
    loader = get_loader(config)
    bundle = _get_bundle(extension, loader)
    asset_path = loader.asset_path
    return src_tags(bundle, asset_path, attrs)


def get_tags_per_page(extension=None, page_name='main', config='DEFAULT', manifest_path=None, attrs=''):
    loader = get_loader(config, manifest_path)
    bundle = _page_bundle(extension, loader, page_name)
    asset_path = loader.asset_path
    return src_tags(bundle, asset_path, attrs)


def get_src_files(extension=None, page_name=None, config='DEFAULT'):
    loader = get_loader(config)
    if page_name:
        bundle = _page_bundle(extension, loader, page_name)
    else:
        bundle = _get_bundle(extension, loader)
    asset_path = loader.asset_path
    return script_paths(bundle, asset_path)
