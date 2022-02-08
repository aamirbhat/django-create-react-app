from create_react_app.config import get_loader
from create_react_app.utils import _filter_by_extension


class AssetTag:
    def __init__(self, public_path):
        self.public_path = public_path

    def css_tag(self, asset_path, attrib="", is_preload=False):
        if is_preload:
            return '<link rel="preload"  href="{0}{1}" {2} as="style" />'.format(self.public_path, asset_path, attrib)
        return '<link type="text/css" href="{0}{1}" rel="stylesheet" {2}/>'.format(self.public_path, asset_path, attrib)

    def script_tag(self, asset_path, attrib="", is_preload=False):
        if is_preload:
            return '<link rel="preload"  href="{0}{1}" {2} as="script" />'.format(self.public_path, asset_path, attrib)
        return '<script type="text/javascript" src="{0}{1}" {2}></script>'.format(self.public_path, asset_path, attrib)

    def src(self, asset_path, **extra):
        return '{0}{1}'.format(self.public_path, asset_path)


class AssetManager(object):
    def __init__(self, config_name):
        self.loader = get_loader(config_name)
        self.asset = AssetTag(self.loader.asset_path)

    def get_bundle(self, extension):
        bundle = self.loader.get_bundle()
        if extension:
            bundle = _filter_by_extension(bundle, extension)
        if not bundle:
            return []
        return bundle

    def get_tag_bundle(self, extension, call_back, ends_with=[], **extra):
        tags = []
        bundle = self.get_bundle(extension=extension)
        for chunk in bundle:
            if not self.loader.is_dev:
                chunk = chunk.replace("static/", "")
            if chunk.endswith(tuple(ends_with)):
                tags.append(call_back(chunk, **extra))
        return tags

    def css_callback(self, chunk, **extra):
        return self.asset.css_tag(chunk, **extra)

    def js_callback(self, chunk, **extra):
        return self.asset.script_tag(chunk, **extra)

    def css_tags(self, **extra):
        return self.get_tag_bundle(extension="css", call_back=self.css_callback, ends_with=['.css', '.css.gz'], **extra)

    def js_tags(self, **extra):
        return self.get_tag_bundle(extension="js", call_back=self.js_callback, ends_with=['.js', '.js.gz'], **extra)


class SrcAssetManager(AssetManager):
    def js_callback(self, chunk, **extra):
        return self.asset.src(chunk, **extra)

    def css_callback(self, chunk, **extra):
        return self.asset.src(chunk, **extra)