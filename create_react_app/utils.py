
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





